import json

with open('./data.json') as MAPPINGS:
    mappings = json.load(MAPPINGS)

USERS = mappings[0]
USER_FEATURES = mappings[1]
LOCATIONS = mappings[2]
LOCATION_FEATURES = mappings[3]
