import pandas as pd

def Data_preprocesser(dataFrame):

    df = dataFrame
    # Handle missing values by filling them with the mean of the column
    df['latitude'].fillna(df['latitude'].mean(), inplace=True)
    df['longitude'].fillna(df['longitude'].mean(), inplace=True)
    
    # Convert categorical 'crime_type' to numerical
    df['victim_gender'] = df['victim_gender'].astype('category').cat.codes
    
    # Convert 'date' and 'time' columns to datetime objects
    df['date'] = pd.to_datetime(df['date'])
    df['time_of_day'] = pd.to_datetime(df['time_of_day'], format='%H:%M:%S').dt.time
    
    # Extract features from 'date' and 'time'
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = pd.to_datetime(df['time_of_day'].astype(str)).dt.hour
    
    # Drop original 'date', 'time', and 'location' columns
    df.drop(columns=['date', 'time_of_day', 'location'], inplace=True)
    
    return df

