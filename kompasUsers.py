import numpy as np
import json
from itertools import islice
from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.evaluation import auc_score
from flask import Flask, request
from waitress import serve
app = Flask(__name__)

from determine_users import find_location_id, find_user_id

import json

import pdb

dataset = Dataset()

with open('./data/locations.json') as locations:
    locations_data = json.load(locations)

with open('./data/users.json') as users:
    users_data = json.load(users)

with open('./data/virtualUsers.json') as virtualUsers:
    virtual_users_data = json.load(virtualUsers)

with open('./data/ratedPlacesAmend.json') as ratings:
    ratings_data = json.load(ratings)

with open('./data/virtualRatings.json') as virtualRatings:
    virtual_ratings_data = json.load(virtualRatings)

full_users = users_data+virtual_users_data
full_ratings = ratings_data+virtual_ratings_data

# create interest list for user features
interests = set([item for sublist in [x['interests'] for x in full_users] for item in sublist])
interestList = list(interests)
# smallInterests = interestList[1:4]
# print(repr(interestList))

# create subCategory list for item features
subCats = set([item for sublist in [x['subCategory'] for x in locations_data] for item in sublist])
subCatList = list(subCats)

# fit the dataset to create mappings for users, items and respective features
dataset.fit((x['_id'] for x in full_users),
(x['_id'] for x in locations_data),user_features=interestList,item_features=subCatList)


# build interactions from ratings data, 'liked' places only at the moment (~350 only)
interactions = dataset.build_interactions(((x['userId'], x['place'], x['weight']) for x in full_ratings))
print(repr(interactions[0]))

# print number of users and items
num_users, num_items = dataset.interactions_shape()
print('Num users: {}, num_items {}.'.format(num_users, num_items))

# buil user features from users interests
user_features = dataset.build_user_features(((x['_id'], x['interests']) for x in full_users),normalize=False)

# buil item features from users iterests
item_features = dataset.build_item_features(((x['_id'], x['subCategory']) for x in locations_data),normalize=False)
# print(repr(item_features))


with open('data.json', 'w') as outfile:
    json.dump(dataset.mapping(), outfile)

model = LightFM(loss='warp', no_components=20)
model.fit(interactions[0], user_features=user_features,item_features=item_features)

train_auc = auc_score(model,
                      interactions[0],
                      user_features=user_features,
                      item_features=item_features,
                      num_threads=2).mean()
print('Hybrid training set AUC: %s' % train_auc)

#turn off debug mode flask

# np.set_printoptions(threshold=np.inf)
@app.route('/recommend/<kompas_user_id>')
def recommend(kompas_user_id):
    try:
        kompas_id = 'ObjectId({})'.format(kompas_user_id)
        user_id = find_user_id(kompas_id)
        score = model.predict(user_id,np.arange(num_items), user_features=user_features,item_features=item_features)
        # np.set_printoptions(threshold=np.inf)
        ranked_items = np.argsort(-score)
        places = find_location_id(ranked_items, score)
        return json.dumps({"userid":kompas_user_id, "places": places, "max_score": max(score), "min_score": min(score)})
    except:
        return json.dumps({"message": "user not in mapping"})

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def hello():
    return "hello world"




serve(app, host='0.0.0.0', port=5000)
# app.run()
