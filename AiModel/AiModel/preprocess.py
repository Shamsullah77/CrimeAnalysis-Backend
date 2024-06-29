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




import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

def preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv('data.csv')
    
    # Print initial data info
    print("Initial Data Info:")
    print(df.info())
    print("\n")

    # Handling missing values
    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    imputer = SimpleImputer(strategy='median')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    
    # Fill categorical columns with the most frequent value
    categorical_cols = df.select_dtypes(include=[object]).columns
    imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_cols] = imputer.fit_transform(df[categorical_cols])
    
    # Convert date column to numeric
    df['date'] = pd.to_datetime(df['date']).map(pd.Timestamp.toordinal)
    
    # Encode categorical variables to numeric
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    # Normalize/Standardize the numeric columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Print processed data info
    print("Processed Data Info:")
    print(df.info())
    print("\n")
    
    # Display the first few rows of the processed data
    print("First few rows of the processed data:")
    print(df.head())
    print("\n")
    
    # Check for any remaining missing values
    print("Check for remaining missing values:")
    print(df.isnull().sum())
    
    # Get the feature names
    feature_names = df.columns.tolist()
    
    return df, label_encoders, scaler, feature_names

if __name__ == "__main__":
    file_path = 'data.csv'  # Change this to your actual file path
    processed_df, encoders, scaler, feature_names = preprocess_data(file_path)
    
    # Save the processed data
    processed_df.to_csv('cleaned_data.csv', index=False)
    print("Data has been processed and saved to 'cleaned_data.csv'.")

    # Save the encoders, scaler, and feature names
    with open('label_encoders_scaler.pkl', 'wb') as f:
        joblib.dump((encoders, scaler, feature_names), f)
    print("Encoders, scaler, and feature names have been saved to 'label_encoders_scaler.pkl'.")
