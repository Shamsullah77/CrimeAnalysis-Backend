# import pandas as pd
# from datetime import datetime
# from sklearn.externals import joblib  # Use joblib for loading your model

# # Function to preprocess the new data
# def preprocess_new_data(df, scaler, feature_names):
#     # Ensure the columns are in the same order as during training
#     df = df[feature_names]
#     # Perform any necessary preprocessing steps here (e.g., encoding categorical variables, scaling numerical features)
#     # Make sure to use the same transformations as during training
    
#     # Example: Assuming you have scaler and label_encoders defined from your preprocessing script
#     df[numeric_cols] = scaler.transform(df[numeric_cols])
#     df[categorical_cols] = df[categorical_cols].apply(lambda col: label_encoders[col.name].transform(col))

#     return df



# # Test data
# test_data = {
#     'date': ['2021-07-06'],
#     'hour_of_day': [24],
#     'location': ['Kandahar Central Park'],
#     'district': ['Center'],
#     'area_name': ['Kandahar Central Park'],
#     'victim_gender': ['Female'],
#     'victim_age': [81],
#     'perpetrator_gender': ['Female'],
#     'perpetrator_age': [67],
#     'weapon': ['None'],
#     'injury': ['Minor'],
#     'weather': ['Cloudy'],
#     'temperature': [15],
#     'previous_activity': ['Walking'],
#     'economical_situation': ['Medium'],
#     'education_level': ['Bachelor'],
#     'latitude': [31.568],
#     'longitude': [65.712],
#     'time_of_day': ['Day'],
#     'day_of_week': ['Monday'],
#     'month': ['June'],
#     'season': ['Summer'],
#     'victim_age_group': ['Adult'],
#     'perpetrator_age_group': ['Adult'],
#     'weather_condition': ['Normal'],
#     'economic_index': [0.8],
#     'education_index': [0.7]
# }

# # Convert test data to DataFrame
# test_df = pd.DataFrame(test_data)

# # Preprocessing steps (ensure these match the preprocessing in your training script)
# # Load necessary preprocessing artifacts (e.g., scaler, label encoders)
# # Example:
# # scaler = joblib.load('scaler.pkl')
# # label_encoders = joblib.load('label_encoders.pkl')
# # feature_names = [...]  # Define the order of features as used during training

# # Assuming you have these variables defined from your preprocessing script
# # Replace these with your actual preprocessing steps
# scaler = None  # Load your scaler here
# label_encoders = None  # Load your label encoders here
# feature_names = None  # Define the feature names order as used during training

# # Preprocess the new data
# if scaler and label_encoders and feature_names:
#     # Preprocess the test data
#     test_df = preprocess_new_data(test_df, scaler, feature_names)

#     # Load your trained model
#     model = joblib.load('your_trained_model.pkl')  # Replace with your actual model file

#     # Make predictions
#     predictions = model.predict(test_df)

#     # Output predictions
#     print("Predictions:", predictions)
# else:
#     print("Error: Preprocessing artifacts or feature names are not properly loaded.")










import pandas as pd
from sklearn.externals import joblib  # Use joblib for loading your model

# Function to preprocess the new data
def preprocess_new_data(df, scaler, label_encoders, feature_names):
    # Ensure the columns are in the same order as during training
    df = df[feature_names]
    
    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    
    # Encode categorical variables
    for col in label_encoders:
        df[col] = label_encoders[col].transform(df[col])
    
    # Normalize/Standardize the numeric columns
    numeric_cols = df.select_dtypes(include=[float, int]).columns
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    
    return df

# Test data
test_data = {
    'date': ['2024-01-27'],
    'hour_of_day': [12],
    'location': ['Central Park'],
    'district': ['Downtown'],
    'area_name': ['City Center'],
    'victim_gender': ['Male'],
    'victim_age': [30],
    'perpetrator_gender': ['Female'],
    'perpetrator_age': [25],
    'weapon': ['Knife'],
    'injury': ['Serious'],
    'weather': ['Clear'],
    'temperature': [25.0],
    'previous_activity': ['Walking'],
    'economical_situation': ['Stable'],
    'education_level': ['Bachelor'],
    'latitude': [40.7128],
    'longitude': [-74.0060],
    'time_of_day': ['Day'],
    'day_of_week': ['Monday'],
    'month': ['June'],
    'season': ['Summer'],
    'victim_age_group': ['Adult'],
    'perpetrator_age_group': ['Adult'],
    'weather_condition': ['Normal'],
    'economic_index': [0.8],
    'education_index': [0.7]
}

# Convert test data to DataFrame
test_df = pd.DataFrame(test_data)

# Load necessary preprocessing artifacts (e.g., scaler, label encoders, feature names)
encoders_scaler_features = joblib.load('label_encoders_scaler.pkl')
label_encoders = encoders_scaler_features[0]
scaler = encoders_scaler_features[1]
feature_names = encoders_scaler_features[2]

# Ensure test data has all the features required
for feature in feature_names:
    if feature not in test_df.columns:
        test_df[feature] = 0  # Add a placeholder value for missing features

# Keep only the features required
test_df = test_df[feature_names]

# Preprocess the new data
preprocessed_df = preprocess_new_data(test_df, scaler, label_encoders, feature_names)

# Load your trained model
model = joblib.load('crime_model_dt.pkl')  # Replace with your actual model file

# Make predictions
predictions = model.predict(preprocessed_df)

# Output predictions along with the location details
for index, prediction in enumerate(predictions):
    location = test_df.iloc[index]['location']
    latitude = test_df.iloc[index]['latitude']
    longitude = test_df.iloc[index]['longitude']
    print(f"Prediction: {prediction}, Location: {location} (Lat: {latitude}, Long: {longitude})")
