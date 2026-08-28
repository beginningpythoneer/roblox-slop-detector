import time
from modules import api
from modules import name_filter

catalog_api_endpoint = "https://catalog.roblox.com/v2/search/items/details"
taxonomy_id = "43H35nJKHzCQM63q3wPaJG"
salesTypeFilter = 1
limit = 120 # Only 10/28/30/60/120

def filter_wrapper(catalog_items):
    for item in catalog_items:
        detection_status = name_filter.filter_asset_name(item[0])

        if detection_status[0]:
            print(f"Possible Slop Detected! Item name: {item[0]}. Detection reason: {detection_status[1]}. Detected keywords: {detection_status[2]}. Item link: https://roblox.com/catalog/{item[1]}")

def api_handler(nextPageCursor = None):
    catalog_items, nextPageCursor = api.get_catalog_items(catalog_api_endpoint, taxonomy_id, salesTypeFilter, limit, nextPageCursor)

    return catalog_items, nextPageCursor

def TheSlopDetector():
    pages = 100
    filtered_pages = 0
    cursor = None

    while filtered_pages < pages:
        try:
            items, cursor = api_handler(cursor)
            if cursor == None:
                print(f"We have came to the end of that thing! Filtered pages: {filtered_pages}.")
                break
            filter_wrapper(items)
            filtered_pages += 1
            time.sleep(0.25)
        except Exception as ex:
            print("Hit an error! Waiting 10 seconds before retrying...")
            time.sleep(10)

if __name__ == "__main__":
    TheSlopDetector()