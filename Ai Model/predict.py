import pickle
import pandas as pd
from preprocess import Data_preprocesser

# Load the model from the file
with open('crime_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Assuming 'X_new' is the new data for which you want to make predictions
df = Data_preprocesser(X_new)
predictions = model.predict(df)
print(predictions)
