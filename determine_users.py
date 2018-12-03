import numpy as np
import json
# import mapping_id
import mapping_id


with open('./data/locations.json') as locations:
    locations_data = json.load(locations)

def find_location_id(ranked_items, scores):
    results = []
    for num in ranked_items:
        place_list = ranked_items.tolist()
        scores_list = scores.tolist()
        for attr, value in mapping_id.LOCATIONS.items():
            if value == num:
                results.append({"place_id" : attr, "rank": place_list.index(num), "score": scores_list[num]})
    return results

def find_location_name(id):
    place = next((x for x in locations_data if x['_id'] == id), None)
    return place

def find_user_id(kompas_user_id):
    print(kompas_user_id)
    for attr, value in mapping_id.USERS.items():
        if attr == kompas_user_id:
            return value
        break
    return value
