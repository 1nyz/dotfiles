import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

dataset = pd.read_csv('Clean_Dataset.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

le = LabelEncoder()
y = le.fit_transform(y)

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0, 1, 2, 3, 4, 5, 6, 7])], remainder = 'passthrough')
x = ct.fit_transform(x).toarray()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))