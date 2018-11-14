import numpy as np
from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k
from lightfm.data import Dataset

import pdb
# Load the MovieLens 100k dataset. Only five
# star ratings are treated as positives
data = fetch_movielens(min_rating=4.0)
ds = data['item_features']
ds = data['item_features']
# print(data['item_feature_labels'])
# print(data)
# print(ds.A)
# print(data['item_labels'])

model = LightFM(loss='warp')
model.fit(data['train'], epochs=50, num_threads=3)


def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape
    print(repr(np.arange(n_items)))


    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        np.set_printoptions(threshold=np.inf)
        print(scores)
        top_items = data['item_labels'][np.argsort(-scores)]
        pdb.set_trace()

        print("User %s" % user_id)
        print(".... Know positives :")

        for x in known_positives[:3]:
            print("         %s" % x)

        print("         Recommended :")

        for x in top_items[:3]:
            print("     %s" % x)


sample_recommendation(model, data, [3, 25, 450])
