# -*- encoding: utf-8 -*-

import pickle
import sqlite3
import numpy as np
import os

# ローカルディレクトリからHasingVectorizerをインポート
from vectorizer import vect


def update_model(db_path, model, batch_size=10000):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("select * from review_db")

    results = c.fetchmany(batch_size)
    while results:
        data = np.array(results)
        X = data[:, 0]
        y = data[:, 1].astype(int)
        classes = np.array([0, 1])
        X_train = vect.transform(X)
        model.partial_fit(X_train, y, classes=classes)
        # next data
        results = c.fetchmany(batch_size)

    conn.close()
    return model

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'),
                       'rb'))
db = os.path.join(cur_dir, 'review.sqlite')

pickle.dump(clf, open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'),
                      'wb'), protocol=pickle.HIGHEST_PROTOCOL)
