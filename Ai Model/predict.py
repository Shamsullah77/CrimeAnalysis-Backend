import pandas as pd
import pickle
from preprocess import clean_and_prepare_data

# Load the new data
new_data = {
    'date': ['2022-10-29'],
    'time_of_day': ['12:15:35'],
    'location': ['2266 Eric Manors North Tabitha'],
    'latitude': [40.7128],
    'longitude': [-74.0060],
    'victim_gender': ['Female'],
    'victim_age': [30],
    'perpetrator_gender': ['Male'],
    'perpetrator_age': [35],
    'weapon': ['Knife'],
    'injury': ['Yes'],
    'weather': ['Clear'],
    'temperature': [75],
    'previous_activity': ['Walking']
}

X_new = pd.DataFrame(new_data)

# Preprocess the new data
X_new_cleaned, _ = clean_and_prepare_data(X_new)

# Load the model and category mappings
with open('crime_model.pkl', 'rb') as file:
    loaded_model, category_mappings = pickle.load(file)

# Ensure X_new_cleaned has the same columns as the training data
model_columns = loaded_model.feature_names_in_ if hasattr(loaded_model, 'feature_names_in_') else X_new_cleaned.columns
X_new_cleaned = X_new_cleaned.reindex(columns=model_columns, fill_value=0)

# Make prediction
prediction = loaded_model.predict(X_new_cleaned)
print("Prediction:", prediction)

# Map the prediction back to the original crime type if needed
reverse_mappings = {v: k for k, v in category_mappings['crime_type'].items()}
predicted_crime_type = reverse_mappings.get(prediction[0], "Unknown")
print("Predicted Crime Type:", predicted_crime_type)















# import pandas as pd
# import pickle
# from preprocess import clean_and_prepare_data

# # Load the new data
# new_data = {
#     'date': ['2022-10-29'],
#     'time_of_day': ['22:30:00'],  # Changed time of day to night time
#     'location': ['1234 Example Street'],  # Changed location
#     'latitude': [34.0522],  # Changed latitude
#     'longitude': [-118.2437],  # Changed longitude
#     'victim_gender': ['Male'],  # Changed victim gender
#     'victim_age': [45],  # Changed victim age
#     'perpetrator_gender': ['Other'],  # Changed perpetrator gender
#     'perpetrator_age': [28],  # Changed perpetrator age
#     'weapon': ['Gun'],  # Changed weapon
#     'injury': ['No'],  # Changed injury status
#     'weather': ['Rainy'],  # Changed weather
#     'temperature': [60],  # Changed temperature
#     'previous_activity': ['Running']  # Changed previous activity
# }


# # new_data = {
# #     'date': ['2022-10-29'],
# #     'time_of_day': ['12:15:35'],
# #     'location': ['2266 Eric Manors North Tabitha'],
# #     'latitude': [40.7128],
# #     'longitude': [-74.0060],
# #     'victim_gender': ['Female'],
# #     'victim_age': [30],
# #     'perpetrator_gender': ['Male'],
# #     'perpetrator_age': [35],
# #     'weapon': ['Knife'],
# #     'injury': ['Yes'],
# #     'weather': ['Clear'],
# #     'temperature': [75],
# #     'previous_activity': ['Walking']
# # }

# X_new = pd.DataFrame(new_data)

# # Preprocess the new data
# X_new_cleaned = clean_and_prepare_data(X_new)

# # Load the model
# with open('crime_model.pkl', 'rb') as file:
#     loaded_model = pickle.load(file)

# # Ensure X_new_cleaned has the same columns as the training data
# model_columns = loaded_model.feature_names_in_
# X_new_cleaned = X_new_cleaned.reindex(columns=model_columns, fill_value=0)

# # Make prediction
# prediction = loaded_model.predict(X_new_cleaned)
# print("Prediction:", prediction)
