import json
from itertools import islice

from lightfm import LightFM
from lightfm.data import Dataset

import pdb

dataset = Dataset()

with open('./newLocations.json') as locations:
    locations_data = json.load(locations)

with open('./interests.json') as interests:
    interests_data = json.load(interests)

with open('./users.json') as users:
    users_data = json.load(users)

with open('./ratedPlacesAmend.json') as ratings:
    ratings_data = json.load(ratings)

for line in islice(locations_data, 2):
    print(json.dumps(line, indent=4))

for line in islice(interests_data, 2):
    print(json.dumps(line, indent=4))

for line in islice(users_data, 2):
    print(json.dumps(line, indent=4))

interestList = set([item for sublist in [x['interests'] for x in users_data] for item in sublist])
dataset.fit((x['userId'] for x in ratings_data),
(x['place'] for x in ratings_data),user_features=interestList)

num_users, num_items = dataset.interactions_shape()
print('Num users: {}, num_items {}.'.format(num_users, num_items))

interactions = dataset.build_interactions(((x['userId'], x['place']) for x in ratings_data))

print(repr(interactions))

# featureSet = Dataset()
# featureSet.fit((x['_id'] for x in users_data),
# (x['interest'] for x in interests_data))
#
# pdb.set_trace()
# user_features = dataset.build_user_features(((x['_id'], x['interests']) for x in users_data))
# print(repr(user_features))

# (interactions, weights) = dataset.build_interactions(((x['_id'], x['firstName'])
#                                                       for x in users_data))
#
# print(repr(interactions))
