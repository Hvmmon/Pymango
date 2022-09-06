import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib


features = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
            "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
            "hours-per-week", "native-country", "income"]


# train_data
data_train = pd.read_csv("adult.data", sep=" ", header=None)
data_train.columns = features
X_train = data_train[features[:-1]]
y_train = data_train["income"]


# fillna with high frequency value
train_mode = dict(X_train.mode().iloc[0])
X_train = X_train.fillna(train_mode)


# test_data
data_test = pd.read_csv("adult.test", sep=" ", header=None)
data_test.columns = features


# convert categoricals
encoders = {}
for column in ['workclass', 'education', 'marital-status',
               'occupation', 'relationship', 'race',
               'sex', 'native-country']:
    enc = LabelEncoder()
    X_train[column] = enc.fit_transform(X_train[column])
    encoders[column] = enc


# convert string to int
for c in features[:-1]:
    if X_train[c].dtypes != "int64":
        X_train[c] = X_train[c].apply(lambda x: x.split(',')[0]).astype('int')


# train the Random Forest algorithm
rf = RandomForestClassifier(n_estimators=100)
rf = rf.fit(X_train, y_train)


# train the Extra Trees algorithm
et = ExtraTreesClassifier(n_estimators=100)
et = et.fit(X_train, y_train)


# save preprocessing objects and weights
joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoders, "./encoders.joblib", compress=True)
joblib.dump(rf, "./random_forest.joblib", compress=True)
joblib.dump(et, "./extra_trees.joblib", compress=True) 