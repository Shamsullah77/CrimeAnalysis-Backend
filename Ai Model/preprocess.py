import pandas as pd

def clean_and_prepare_data(df):
    # Handle missing values
    if 'latitude' in df.columns:
        df['latitude'] = df['latitude'].fillna(df['latitude'].mean())
    if 'longitude' in df.columns:
        df['longitude'] = df['longitude'].fillna(df['longitude'].mean())

    # Convert categorical columns to numeric codes
    categorical_columns = ['crime_type', 'victim_gender', 'perpetrator_gender', 'weapon', 'injury', 'weather', 'previous_activity']
    category_mappings = {}
    for column in categorical_columns:
        if column in df.columns:
            df[column] = df[column].astype('category')
            category_mappings[column] = dict(enumerate(df[column].cat.categories))
            df[column] = df[column].cat.codes

    # Convert date and time to separate components
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
    
    if 'time_of_day' in df.columns:
        df['time_of_day'] = pd.to_datetime(df['time_of_day'], format='%H:%M:%S').dt.time
        df['hour'] = pd.to_datetime(df['time_of_day'].astype(str), format='%H:%M:%S').dt.hour

    # Drop the original date and time columns if they exist
    columns_to_drop = ['date', 'time_of_day', 'location']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    
    return df, category_mappings




# import pandas as pd

# def clean_and_prepare_data(df):
#     # Handle missing values
#     if 'latitude' in df.columns:
#         df['latitude'] = df['latitude'].fillna(df['latitude'].mean())
#     if 'longitude' in df.columns:
#         df['longitude'] = df['longitude'].fillna(df['longitude'].mean())

#     # Convert categorical columns to numeric codes
#     categorical_columns = ['crime_type', 'victim_gender', 'perpetrator_gender', 'weapon', 'injury', 'weather', 'previous_activity']
#     for column in categorical_columns:
#         if column in df.columns:
#             df[column] = df[column].astype('category').cat.codes

#     # Convert date and time to separate components
#     if 'date' in df.columns:
#         df['date'] = pd.to_datetime(df['date'])
#         df['year'] = df['date'].dt.year
#         df['month'] = df['date'].dt.month
#         df['day'] = df['date'].dt.day
    
#     if 'time_of_day' in df.columns:
#         df['time_of_day'] = pd.to_datetime(df['time_of_day'], format='%H:%M:%S').dt.time
#         df['hour'] = pd.to_datetime(df['time_of_day'].astype(str), format='%H:%M:%S').dt.hour

#     # Drop the original date and time columns if they exist
#     columns_to_drop = ['date', 'time_of_day', 'location']
#     df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    
#     return df
