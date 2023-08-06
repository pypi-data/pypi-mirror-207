
from dacite import from_dict
from dataclasses import dataclass, field


from gandai.models import Event, Company, Checkpoint
from gandai import query

from gandai.sources import GrataWrapper as grata




def process_event(e: Event) -> None:
    print(e)
    search_uid = e.search_uid
    search = query.find_search_by_uid(search_uid)

    if e.type == "create":
        pass
    elif e.type == "advance":
        # enrich the company
        company = query.find_company_by_domain(e.domain)
        resp = grata.enrich(company.domain)
        if resp.get("status") == 404:
            print(f"{company} not found")
        else:
            print(resp)
            company.name = resp.get("name")
            company.description = resp.get("description")
            company.meta = company.meta | resp # merge 
            query.update_company(company)


    elif e.type == "validate":
        # find similar companies

        companies = grata.find_similar(domain=e.domain, search=search)
        
        for company in companies:
            print(company)
            # first make sure the company is there
            query.insert_company(
                Company(
                    domain=company["domain"],
                    name=company.get("name"),
                    description=company.get("description"),
                    # meta=company, # merge this?
                )
            )

            # and "create"
            query.insert_event(
                Event(
                    search_uid=search_uid,
                    domain=company.get("domain"),
                    actor_key="gratabot",
                    type="create",
                )
            )
            # suggestions = suggestions.extend(
            #     source_scrub.find_similar(domain=e.domain, search=search)
            # )

            # caching for page token
            # TBD if I care
            # query.insert_event(
            #     Event(
            #         domain=e.domain,
            #         search_uid=search_uid,
            #         type="generate",
            #         actor_key="gratabot",
            #         data=suggestions,
            #     )
            # )

    elif e.type == "send":
        pass
    elif e.type == "accept":
        pass
    elif e.type == "reject":
        pass
    elif e.type == "conflict":
        pass
    
    elif e.type == "criteria":
        pass
    
    # finally, record we processed the event
    query.insert_checkpoint(Checkpoint(event_id=e.id))


def process_events(search_uid: int) -> int:
    """
    Process all events for a given search
    Could tidy
    """
    events = []

    for event in query.event(search_uid).to_dict(orient='records'):
        # event["data"] = json.loads(event["data"])
        event = from_dict(Event, event)
        events.append(event)
        print(event)

    checkpoints = query.checkpoint()
    processed_count = 0
    for e in events:
        if e.id not in checkpoints["event_id"]:
            process_event(e)
            processed_count += 1

    return processed_count
