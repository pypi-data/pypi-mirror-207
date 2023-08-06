import json
import pandas as pd
import polars as pl
from dataclasses import asdict
from dacite import from_dict
from gandai.models import (
    Event,
    Company,
    EventType,
    Actor,
    Search,
    Checkpoint,
)


import os
import sqlalchemy
from sqlalchemy import text
from google.cloud.sql.connector import Connector
from dotenv import load_dotenv

load_dotenv()


def get_engine():
    print(os.getenv("ENV_STAGE"))
    if os.getenv("ENV_STAGE") == "local":
        DB_URI = "postgresql://postgres@localhost/parker"
        return sqlalchemy.create_engine(DB_URI)
    elif os.getenv("ENV_STAGE") == "dev":
        
        connector = Connector()
        def getconn():
            conn = connector.connect(
                os.getenv("INSTANCE_CONNECTION_NAME"),
                "pg8000",
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                db=os.getenv("DB_NAME"),
            )
            return conn
        pool = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=getconn,
        )
        return pool


engine = get_engine()


### WRITES ###


def insert_company(company: Company):
    with engine.connect() as con:
        statement = text(
            """
                INSERT INTO company (domain, name, description) 
                VALUES(:domain, :name, :description)
                ON CONFLICT DO NOTHING
            """
        )
        con.execute(statement, asdict(company))
        con.commit()
    return company


def insert_event(event: Event) -> Event:
    with engine.connect() as con:
        statement = text(
            """
                INSERT INTO event (search_uid, domain, actor_key, type, data) 
                VALUES(:search_uid, :domain, :actor_key, :type, :data)
                ON CONFLICT DO NOTHING
                RETURNING id
            """
        )
        obj = asdict(event)
        obj["data"] = json.dumps(obj["data"])
        result = con.execute(statement, obj)
        # print(result.first())
        _id = result.first()
        event.id = _id[0] if _id else None
        con.execute(text("REFRESH MATERIALIZED VIEW target"))
        con.commit()
    return event


def insert_actor(actor: Actor) -> Actor:
    with engine.connect() as con:
        statement = text(
            """
                INSERT INTO actor (key, type, name) 
                VALUES(:key, :type, :name)
                ON CONFLICT DO NOTHING
            """
        )
        obj = asdict(actor)
        con.execute(statement, obj)
        con.commit()
    return actor


def insert_search(search: Search) -> Search:
    with engine.connect() as con:
        statement = text(
            """
                INSERT INTO search (uid, client_domain, label, meta, inclusion, exclusion, sort) 
                VALUES(:uid, :client_domain, :label, :meta, :inclusion, :exclusion, :sort)
                ON CONFLICT DO NOTHING
            """
        )
        obj = asdict(search)
        obj["meta"] = json.dumps(obj["meta"])
        obj["inclusion"] = json.dumps(obj["inclusion"])
        obj["exclusion"] = json.dumps(obj["exclusion"])
        obj["sort"] = json.dumps(obj["sort"])
        con.execute(statement, obj)
        con.commit()
    return search


def insert_checkpoint(checkpoint: Checkpoint) -> Checkpoint:
    with engine.connect() as con:
        statement = text(
            """
                INSERT INTO checkpoint (event_id) 
                VALUES(:event_id)
            """
        )
        con.execute(statement, asdict(checkpoint))
        con.commit()
    return checkpoint


### READS ###


def search():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT *, meta->>'group' as group FROM search"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df


def target(search_uid: int, last_event_type: str = "advance"):
    with engine.connect() as conn:
        statement = "SELECT * FROM target WHERE search_uid = :search_uid AND last_event_type = :last_event_type"
        result = conn.execute(
            text(statement),
            {"search_uid": search_uid, "last_event_type": last_event_type},
        )
        targets = pd.DataFrame(result.fetchall(), columns=result.keys())
    
    comments = comment_by_domain(search_uid)
    targets = targets.merge(comments, on="domain", how="left")
    
    
    # handle sorting
    search = find_search_by_uid(search_uid)
    targets = targets.sort_values(
        by=search.sort.get("field", "domain"), 
        ascending=search.sort.get("order") == "asc"
    )
    
    
    return targets


def target_count(search_uid: int) -> pd.DataFrame:
    with engine.connect() as conn:
        statement = """
                SELECT last_event_type, count(*)
                FROM target
                WHERE search_uid = :search_uid
                GROUP BY last_event_type
            """
        result = conn.execute(
            text(statement),
            {"search_uid": search_uid},
        )
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df


def event(search_uid: int) -> pd.DataFrame:
    with engine.connect() as conn:
        statement = """
                SELECT *
                FROM event
                WHERE search_uid = :search_uid
            """
        result = conn.execute(text(statement), {"search_uid": search_uid})
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df


def checkpoint() -> pd.DataFrame:
    with engine.connect() as conn:
        statement = """
                SELECT *
                FROM checkpoint
            """
        result = conn.execute(text(statement))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df


def comment_by_domain(search_uid: int) -> pd.DataFrame:
    with engine.connect() as conn:
        statement = """
                SELECT *, data->>'comment' AS comment
                FROM event e
                WHERE 
                    search_uid = :search_uid AND
                    type = 'comment'
            """
        result = conn.execute(
            text(statement),
            {"search_uid": search_uid},
        )
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    return df.groupby("domain").agg({"comment": lambda x: list(x)}).reset_index()


### FINDERS -> dataclass ###


def find_search_by_uid(search_uid: int) -> Search:
    with engine.connect() as conn:
        statement = """
                SELECT *
                FROM search
                WHERE uid = :search_uid
            """
        result = conn.execute(text(statement), {"search_uid": search_uid})

    if result.rowcount == 0:
        return None
    else:
        obj = dict(zip(result.keys(), result.fetchone()))
        return from_dict(Search, obj)


def find_company_by_domain(domain: str) -> Company:
    with engine.connect() as conn:
        statement = """
                SELECT *
                FROM company
                WHERE domain = :domain
            """
        result = conn.execute(text(statement), {"domain": domain})
        # obj = dict(zip(result.keys(), result.fetchone()))
    if result.rowcount == 0:
        return None
    else:
        obj = dict(zip(result.keys(), result.fetchone()))
        return from_dict(Company, obj)


### UPDATE ###


def update_company(company: Company) -> None:
    with engine.connect() as conn:
        statement = """
            UPDATE company
            SET
                name = :name,
                description = :description,
                meta = :meta
            WHERE domain = :domain
            """

        conn.execute(
            text(statement),
            {
                "name": company.name,
                "description": company.description,
                "domain": company.domain,
                "meta": json.dumps(company.meta),
            },
        )
        conn.execute(text("REFRESH MATERIALIZED VIEW target"))
        conn.commit()


def update_search(search: Search) -> None:
    with engine.connect() as conn:
        conn.execute(
            text(
                """
                UPDATE search
                SET
                    sort = :sort,
                    inclusion = :inclusion,
                    exclusion = :exclusion
                WHERE uid = :uid
                """
            ),
            {
                "sort": json.dumps(search.sort),
                "inclusion": json.dumps(search.inclusion),
                "exclusion": json.dumps(search.exclusion),
                "uid": search.uid,
            },
        )
        conn.commit()


## Fix before production
# con = engine.connect()

# def target(search_uid: int, last_event_type: str = None) -> pl.DataFrame:
#     assert isinstance(search_uid, int)
#     assert last_event_type in [
#         None,
#         "create",
#         "advance",
#         "validate",
#         "send",
#         "accept",
#         "reject",
#         "conflict",
#     ]
#     if last_event_type is None:
#         query = f"""
#             SELECT *
#             FROM target t
#             WHERE search_uid = {search_uid}
#         """
#     else:
#         query = f"""
#                 SELECT *
#                 FROM target t
#                 WHERE search_uid = {search_uid} AND last_event_type = '{last_event_type}'
#             """
#     # targets = pl.read_database(query, DB_URI)
#     targets = pd.read_sql(sqlalchemy.text(query), con)
#     return targets


# def target_count(search_uid: int) -> pl.DataFrame:
#     assert isinstance(search_uid, int)
#     query = f"""
#             SELECT last_event_type, count(*)
#             FROM target
#             WHERE search_uid = {search_uid}
#             GROUP BY last_event_type
#         """
#     counts = pd.read_sql(sqlalchemy.text(query), con)
#     return counts


# def event(search_uid: int = None) -> pl.DataFrame:
#     # assert isinstance(search_uid, int)
#     if search_uid is None:
#         query = f"""
#             SELECT *
#             FROM event
#         """
#     else:
#         query = f"""
#                 SELECT *
#                 FROM event
#                 WHERE search_uid = {search_uid}
#             """
#     events = pd.read_sql(sqlalchemy.text(query), con)
#     return events


# def checkpoint() -> pl.DataFrame:
#     query = f"""
#             SELECT *
#             FROM checkpoint
#         """
#     checkpoints = pd.read_sql(sqlalchemy.text(query), con)
#     return checkpoints


# def comment(search_uid: int) -> pl.DataFrame:
#     assert isinstance(search_uid, int)
#     query = f"""
#             SELECT *
#             FROM event
#             WHERE type = 'comment'
#         """
#     comments = pd.read_sql(sqlalchemy.text(query), con)
#     return comments


# def comment_by_domain(search_uid: int) -> pl.DataFrame:
#     assert isinstance(search_uid, int)
#     query = f"""
#             SELECT
#                 e.search_uid,
#                 e.domain,
#                 e.actor_key,
#                 e.created,
#                 e.data->>'comment' AS comment
#             FROM
#                 event e
#             WHERE
#                 e.type = 'comment' AND
#                 e.search_uid = {search_uid}
#         """
#     comments = pd.read_sql(sqlalchemy.text(query), con)
#     comments = comments.groupby("domain").agg({"comment": lambda x: list(x)})
#     print(comments)
#     return comments


# def searches() -> pl.DataFrame:
#     query = f"""
#             SELECT *, meta->>'group' as group
#             FROM search
#         """
#     searches = pd.read_sql(sqlalchemy.text(query), con)
#     return searches


# def find_search_by_uid(uid: int) -> Search:
#     query = f"""
#             SELECT *
#             FROM search
#             WHERE uid = {uid}
#         """
#     # with engine
#     obj = dict(pd.read_sql(sqlalchemy.text(query), con).loc[0])
#     obj["uid"] = int(obj["uid"])
#     obj["client_id"] = int(obj["client_id"])
#     # obj["meta"] = json.loads(obj["meta"])
#     # obj["inclusion"] = json.loads(obj["inclusion"])
#     # obj["exclusion"] = json.loads(obj["exclusion"])
#     # obj["sort"] = json.loads(obj["sort"])
#     return from_dict(Search, obj)


# def find_company_by_domain(domain: str) -> Company:
#     query = f"""
#             SELECT *
#             FROM company
#             WHERE domain = '{domain}'
#         """
#     obj = dict(pd.read_sql(sqlalchemy.text(query), con).loc[0])
#     # obj["uid"] = int(obj["uid"])
#     # obj = pl.read_database(query, DB_URI).to_dicts()[0]
#     # obj["meta"] = json.loads(obj["meta"])
#     return from_dict(Company, obj)


## Writes with psycopg2

# conn = psycopg2.connect("dbname=parker user=postgres")
# cur = conn.cursor()


# def insert_event(event: Event) -> Event:
#     """Inserts an event into the database. If the company does not exist, it is inserted as well."""

#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             SELECT domain FROM company WHERE domain = %s
#             """,
#             (event.domain,),
#         )
#         result = cur.fetchone()
#         if result is None:
#             # If company does not exist, insert it
#             print(f"Inserting company {event.domain}")
#             insert_company(Company(domain=event.domain, name=""))

#         cur.execute(
#             """
#             INSERT INTO event (search_uid, domain, actor_key, type, data)
#             VALUES (%s, %s, %s, %s, %s)
#             ON CONFLICT DO NOTHING
#         """,
#             (
#                 event.search_uid,
#                 event.domain,
#                 event.actor_key,
#                 event.type,
#                 json.dumps(event.data),
#             ),
#         )
#         cur.execute("REFRESH MATERIALIZED VIEW target")  # yasss
#     conn.commit()
#     return event


# def insert_company(company: Company) -> Company:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             INSERT INTO company (domain, name, description, meta)
#             VALUES (%s, %s, %s, %s)
#             ON CONFLICT (domain) DO NOTHING;
#         """,
#             (
#                 company.domain,
#                 company.name,
#                 company.description,
#                 json.dumps(company.meta),
#             ),
#         )
#     conn.commit()
#     return company


# def insert_checkpoint(checkpoint: Checkpoint) -> Checkpoint:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             INSERT INTO checkpoint (event_id)
#             VALUES (%s)
#             """,
#             (checkpoint.event_id,),
#         )
#     conn.commit()
#     return checkpoint


# def insert_search(search: Search) -> Search:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             INSERT INTO search (uid, client_id, label, meta, inclusion, exclusion, sort)
#             VALUES (%s, %s, %s, %s, %s, %s, %s)
#             ON CONFLICT (uid) DO NOTHING;
#         """,
#             (
#                 search.uid,
#                 search.client_id,
#                 search.label,
#                 json.dumps(search.meta),
#                 json.dumps(search.inclusion),
#                 json.dumps(search.exclusion),
#                 json.dumps(search.sort),
#             ),
#         )
#     conn.commit()
#     return search


# def insert_client(client: Client) -> None:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             INSERT INTO client (name, description)
#             VALUES (%s, %s)
#             ON CONFLICT (name) DO NOTHING;
#         """,
#             (client.name, client.description),
#         )
#     conn.commit()


# def insert_actor(actor: Actor) -> Actor:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             INSERT INTO actor (key, type, name)
#             VALUES (%s, %s, %s)
#             ON CONFLICT (key) DO NOTHING;
#         """,
#             (actor.key, actor.type, actor.name),
#         )
#     conn.commit()
#     return actor


# def update_search(search: Search) -> Search:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             UPDATE search
#             SET
#                 client_id = %s,
#                 label = %s,
#                 meta = %s,
#                 inclusion = %s,
#                 exclusion = %s,
#                 sort = %s
#             WHERE uid = %s
#         """,
#             (
#                 search.client_id,
#                 search.label,
#                 json.dumps(search.meta),
#                 json.dumps(search.inclusion),
#                 json.dumps(search.exclusion),
#                 json.dumps(search.sort),
#                 search.uid,
#             ),
#         )
#     conn.commit()
#     return search

# def update_company(company: Company) -> Company:
#     with conn.cursor() as cur:
#         cur.execute(
#             """
#             UPDATE company
#             SET
#                 name = %s,
#                 description = %s,
#                 meta = %s
#             WHERE domain = %s
#         """,
#             (
#                 company.name,
#                 company.description,
#                 json.dumps(company.meta),
#                 company.domain,
#             ),
#         )
#     conn.commit()
#     return company
