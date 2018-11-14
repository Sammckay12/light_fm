import numpy as np
import json
# import mapping_id
import virtual_mapping


with open('./data/locations.json') as locations:
    locations_data = json.load(locations)

def find_location_id(ranked_items):
    for num in ranked_items[:15]:
        for attr, value in virtual_mapping.LOCATIONS.items():
            if value == num:
                find_location_name(attr)
                print(attr, value)

def find_location_name(id):
    place = next((x for x in locations_data if x['_id'] == id), None)
    print(place['name'])
