# -*- coding: utf-8 -*-
import pandas as pd

import sklearn as sk

"""add data set"""

pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
mushroom = fetch_ucirepo(id=73)

# data (as pandas dataframes)
X = mushroom.data.features
y = mushroom.data.targets

# metadata
print(mushroom.metadata)

# variable information
print(mushroom.variables)

"""fix x and y"""

X

x = pd.get_dummies( X , dtype = float)

x

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

y

"""add train_test_split and make x_train ans test and y"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train , y_test = train_test_split(x,y, random_state=35 ,test_size= 0.2 , shuffle=True )

"""add Randomforest c  and r fit and score"""

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators= 10 , random_state=35)

print(x_test_array.shape)
print(y_test.shape)

rf.fit(x_train, y_train)

rf.score(x_test , y_test)

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators= 1000 , random_state=35 , max_depth=100 , min_samples_split=8)

rf.fit(x_train, y_train)

rf.score(x_test , y_test)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.countplot(x=y)
plt.title('Count of Each Class in the Mushroom Dataset')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()

dt.fit(x_train , y_train)

dt.score(x_test , y_test)

from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor( max_depth=100 , min_samples_split=2)

dt.fit(x_train , y_train)

dt.score(x_test , y_test)

from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier( subsample=1.0 , min_samples_split=2)

gb.fit(x_train , y_train)

gb.score(x_test , y_test)

from sklearn.ensemble import GradientBoostingRegressor
gbr = GradientBoostingRegressor( subsample=1.0 , min_samples_split=2)

gbr.fit(x_train , y_train)

gbr.score(x_test , y_test)













