import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer

dataset = pd.read_csv('Clean_Dataset.csv')

ct = ColumnTransformer([('encoder', OneHotEncoder(), [1, 2, 3, 4, 5 ,6, 7, 8])], remainder = 'passthrough')
dataset = ct.fit_transform(dataset).toarray()
print(dataset)