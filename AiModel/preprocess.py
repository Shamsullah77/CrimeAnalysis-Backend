# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.impute import SimpleImputer
# import joblib

# def preprocess_data(file_path):
#     # Load the dataset
#     df = pd.read_csv('data.csv')
    
#     # Print initial data info
#     print("Initial Data Info:")
#     print(df.info())
#     print("\n")

#     # Handling missing values
#     # Fill numeric columns with median
#     numeric_cols = df.select_dtypes(include=[np.number]).columns
#     imputer = SimpleImputer(strategy='median')
#     df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    
#     # Fill categorical columns with the most frequent value
#     categorical_cols = df.select_dtypes(include=[object]).columns
#     imputer = SimpleImputer(strategy='most_frequent')
#     df[categorical_cols] = imputer.fit_transform(df[categorical_cols])
    
#     # Convert date column to numeric
#     df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    
#     # Encode categorical variables to numeric
#     label_encoders = {}
#     for col in categorical_cols:
#         le = LabelEncoder()
#         df[col] = le.fit_transform(df[col])
#         label_encoders[col] = le
    
#     # Normalize/Standardize the numeric columns
#     scaler = StandardScaler()
#     df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
#     # Print processed data info
#     print("Processed Data Info:")
#     print(df.info())
#     print("\n")
    
#     # Display the first few rows of the processed data
#     print("First few rows of the processed data:")
#     print(df.head())
#     print("\n")
    
#     # Check for any remaining missing values
#     print("Check for remaining missing values:")
#     print(df.isnull().sum())
    
#     return df, label_encoders, scaler

# if __name__ == "__main__":
#     file_path = 'data.csv'  # Change this to your actual file path
#     processed_df, encoders, scaler = preprocess_data(file_path)
    
#     # Save the processed data
#     processed_df.to_csv('cleaned_data.csv', index=False)
#     print("Data has been processed and saved to 'cleaned_data.csv'.")

#     # Save the encoders and scaler
#     with open('label_encoders_scaler.pkl', 'wb') as f:
#         joblib.dump((encoders, scaler), f)
#     print("Encoders and scaler have been saved to 'label_encoders_scaler.pkl'.")



# def preprocess_new_data(new_data, label_encoders, scaler, feature_names):
#     # Convert the new data into a DataFrame
#     df = pd.DataFrame(new_data)

#     # Convert date column to numeric
#     df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)

#     # Encode categorical variables using the provided label encoders
#     for col, le in label_encoders.items():
#         if col in df.columns:
#             df[col] = df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

#     # Fill missing numeric columns with 0 (or other appropriate strategy)
#     numeric_cols = df.select_dtypes(include=[np.number]).columns
#     df[numeric_cols] = df[numeric_cols].fillna(0)

#     # Normalize/Standardize the numeric columns using the provided scaler
#     df[numeric_cols] = scaler.transform(df[numeric_cols])

#     # Ensure the order and presence of columns match the feature_names used during training
#     df = df[feature_names]

#     return df, label_encoders, scaler, feature_names



import os
import pandas as pd
import joblib
from data_preprocessor import DataPreprocessor  # Import the class

def preprocess_data(file_path):
    # Load and inspect data
    traindf = pd.read_csv('data.csv')

    # Ensure correct data types
    traindf['victim_age'] = pd.to_numeric(traindf['victim_age'], errors='coerce')
    traindf['perpetrator_age'] = pd.to_numeric(traindf['perpetrator_age'], errors='coerce')
    traindf['economic_index'] = pd.to_numeric(traindf['economic_index'], errors='coerce')
    traindf['education_index'] = pd.to_numeric(traindf['education_index'], errors='coerce')

    numeric_features = ['victim_age', 'perpetrator_age', 'economic_index', 'education_index']
    categorical_features = ['victim_gender', 'perpetrator_gender', 'weapon', 'weather_condition']

    data_preprocessor = DataPreprocessor(numeric_features, categorical_features)

    X = traindf.drop(['crime_type', 'location'], axis=1)
    y_crime_type = traindf['crime_type'].astype(str)
    y_location = traindf['location'].astype(str)

    X[numeric_features] = X[numeric_features].fillna(X[numeric_features].mean())
    X[categorical_features] = X[categorical_features].fillna('Unknown')

    data_preprocessor.fit(X)
    X_preprocessed = data_preprocessor.transform(X)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    joblib.dump(data_preprocessor, os.path.join(current_dir, 'column_transformer.pkl'))
    joblib.dump((X_preprocessed, y_crime_type, y_location), os.path.join(current_dir, 'preprocessed_data.pkl'))

    return X_preprocessed, y_crime_type, y_location

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    preprocess_data(os.path.join(current_dir, 'data.csv'))
    print("Preprocessing complete.")
