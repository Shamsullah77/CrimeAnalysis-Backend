import joblib
import pandas as pd
import numpy as np
import json
import os
from data_preprocessor import DataPreprocessor  # Import the class

# Define the base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Load the column transformer and models using absolute paths
col_tsf = joblib.load(os.path.join(base_path, 'column_transformer.pkl'))
model_crime_type = joblib.load(os.path.join(base_path, 'final_random_forest_model_for_crime_type.pkl'))
model_location = joblib.load(os.path.join(base_path, 'final_random_forest_model_for_location.pkl'))

def predict_top_5_crime_and_location(data):
    # Preprocess the input data
    data_preprocessed = col_tsf.transform(data)

    # Predict crime type probabilities
    crime_type_prob = model_crime_type.predict_proba(data_preprocessed)
    # Predict location probabilities
    location_prob = model_location.predict_proba(data_preprocessed)

    # Get the top 5 predictions for crime type and location with probabilities
    top_crime_indices = crime_type_prob.argsort(axis=1)[:, -5:][:, ::-1]
    top_crime_probs = np.sort(crime_type_prob, axis=1)[:, -5:][:, ::-1]
    
    top_5_location_indices = location_prob.argsort(axis=1)[:, -5:][:, ::-1]
    top_5_location_probs = np.sort(location_prob, axis=1)[:, -5:][:, ::-1]

    results = []
    num_crime_classes = top_crime_indices.shape[1]
    num_location_classes = top_5_location_indices.shape[1]
    
    for i in range(num_location_classes):
        result = {
            'crime_type_prediction': model_crime_type.classes_[top_crime_indices[0, i % num_crime_classes]],
            'crime_type_probability': round(top_crime_probs[0, i % num_crime_classes], 4),
            'location_prediction': model_location.classes_[top_5_location_indices[0, i]],
            'location_probability': round(top_5_location_probs[0, i], 4)
        }
        results.append(result)

    return results

if __name__ == "__main__":
    # Example input data
    input_data = {
        'hour_of_day': [20],
        'victim_age': [18],
        'perpetrator_age': [41],
        'economic_index': [88.1],
        'education_index': [38.7],
        'date': ['2020-09-12'],
        'location': ['center'],
        'victim_gender': ['Male'],
        'perpetrator_gender': ['Male'],
        'weapon': ['Other'],
        'time_of_day': ['Night'],
        'day_of_week': ['Saturday'],
        'month': ['September'],
        'season': ['Winter'],
        'victim_age_group': ['Child'],
        'perpetrator_age_group': ['Adult'],
        'weather_condition': ['Wet'],
    }

    input_data = pd.DataFrame(input_data)
    predictions = predict_top_5_crime_and_location(input_data)
    
    # Print each of the top 5 predictions as separate JSON objects
    for prediction in predictions:
        print(json.dumps(prediction))
