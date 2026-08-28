import requests

def get_catalog_items(catalog_api_endpoint, taxonomy_id, salesTypeFilter, limit, nextPageCursor = None):
    filled_api_link = f"{catalog_api_endpoint}?taxonomy={taxonomy_id}&salesTypeFilter={salesTypeFilter}&limit={limit}"
    if nextPageCursor:
        filled_api_link += f"&cursor={nextPageCursor}"

    resp = requests.get(filled_api_link)
    resp.raise_for_status()
    json = resp.json()

    next_page_cursor = json["nextPageCursor"]

    catalog_items = []

    for item in json["data"]:
        catalog_items.append((item["name"], item["id"]))

    return (catalog_items, next_page_cursor)