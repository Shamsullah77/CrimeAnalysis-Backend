import joblib
import pandas as pd
import json
import os
from data_preprocessor import DataPreprocessor  # Import the class

# Define the base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Load the column transformer and models using absolute paths
col_tsf = joblib.load(os.path.join(base_path, 'column_transformer.pkl'))
model_crime_type = joblib.load(os.path.join(base_path, 'final_random_forest_model_for_crime_type.pkl'))
model_location = joblib.load(os.path.join(base_path, 'final_random_forest_model_for_location.pkl'))

def predict_crime_and_location(data):
    # Preprocess the input data
    data_preprocessed = col_tsf.transform(data)

    # Predict crime type
    crime_type_pred = model_crime_type.predict(data_preprocessed)
    crime_type_prob = model_crime_type.predict_proba(data_preprocessed)

    # Predict location
    location_pred = model_location.predict(data_preprocessed)
    location_prob = model_location.predict_proba(data_preprocessed)

    # Get the prediction with the highest probability for crime type and location
    crime_type_max_prob_idx = crime_type_prob.argmax(axis=1)
    location_max_prob_idx = location_prob.argmax(axis=1)

    # Create a response with predictions and their respective highest probabilities
    result = {
        'crime_type_prediction': crime_type_pred[0],
        'crime_type_probability': round(crime_type_prob[0][crime_type_max_prob_idx[0]], 4),
        'location_prediction': location_pred[0],
        'location_probability': round(location_prob[0][location_max_prob_idx[0]], 4)
    }

    return result

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
    predictions = predict_crime_and_location(input_data)
    print(json.dumps(predictions))
