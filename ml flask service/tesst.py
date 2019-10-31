import pickle


# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))
print(model.predict([[12000, 25, 1, 2, 1]]))