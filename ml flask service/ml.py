# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

dataset = pd.read_excel('krediVeriseti.xlsx')
X = dataset.iloc[:, :5]
y = dataset.iloc[:, 5]
X_original = dataset.iloc[:, :5]
y_original = dataset.iloc[:, 5]

# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X.iloc[:, 2] = labelencoder_X.fit_transform(X.iloc[:, 2])
X.iloc[:, 4] = labelencoder_X.fit_transform(X.iloc[:, 4])
# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# our model
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Saving model using pickle
pickle.dump(classifier, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))

