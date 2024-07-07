import random
import pandas as pd
from datetime import datetime, timedelta
from imblearn.over_sampling import SMOTE

# List of predefined locations
locations = [
    "Center", "Kharkrez", "Maruf", "Spin Boldak", "Daman", 
    "Arghistan", "Panjwayi", "Maywand", "Shah Wali Kot", 
    "Zhari", "Nesh", "Reag"
]

# Generate random data
num_records = 12000
data = []
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 1, 1)

for _ in range(num_records):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    hour_of_day = random.randint(1, 24)
    
    location = random.choice(locations)
    
    victim_gender = random.choice(['Male', 'Female'])
    victim_age = random.randint(1, 100)
    perpetrator_gender = random.choice(['Male', 'Female'])
    perpetrator_age = random.randint(10, 100)
    weapon = random.choice(['Knife', 'Gun', 'None', 'Other'])
    injury = random.choice(['None', 'Minor', 'Severe', 'Fatal'])
    weather = random.choice(['Clear', 'Rainy', 'Snowy', 'Cloudy'])
    temperature = random.uniform(-10, 40)
    previous_activity = random.choice(['Walking', 'Driving', 'Shopping', 'Working'])
    economical_situation = random.choice(['Low', 'Medium', 'High'])
    education_level = random.choice(['None', 'Primary', 'Secondary', 'Tertiary'])
    crime_type = random.choice(['Theft', 'Kill'])
    time_of_day = random.choice(['Morning', 'Afternoon', 'Evening', 'Night'])
    day_of_week = date.strftime("%A")
    month = date.strftime("%B")
    season = random.choice(['Winter', 'Spring', 'Summer', 'Fall'])
    victim_age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])
    perpetrator_age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])
    weather_condition = random.choice(['Dry', 'Wet'])
    economic_index = random.uniform(0, 100)
    education_index = random.uniform(0, 100)

    data.append([
        date, hour_of_day, location, victim_gender, victim_age,
        perpetrator_gender, perpetrator_age, weapon, injury, weather, temperature, previous_activity,
        economical_situation, education_level, crime_type, time_of_day, day_of_week, 
        month, season, victim_age_group, perpetrator_age_group, weather_condition, economic_index, education_index
    ])

# Define column names (without latitude, longitude, district, area_name)
columns = [
    'date', 'hour_of_day', 'location', 'victim_gender', 'victim_age',
    'perpetrator_gender', 'perpetrator_age', 'weapon', 'injury', 'weather', 'temperature', 
    'previous_activity', 'economical_situation', 'education_level', 'crime_type',
    'time_of_day', 'day_of_week', 'month', 'season', 'victim_age_group', 'perpetrator_age_group', 
    'weather_condition', 'economic_index', 'education_index'
]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Convert date to a numerical value
df['date'] = df['date'].apply(lambda x: x.timestamp())

# Separate categorical and numerical columns
categorical_columns = ['location', 'victim_gender', 'perpetrator_gender', 'weapon', 'injury', 'weather', 'previous_activity', 'economical_situation', 'education_level', 'time_of_day', 'day_of_week', 'month', 'season', 'victim_age_group', 'perpetrator_age_group', 'weather_condition']
numerical_columns = df.columns.difference(categorical_columns + ['crime_type'])

# Balance the dataset (assuming 'crime_type' is the target variable)
X = df[numerical_columns]
y = df['crime_type']

smote = SMOTE()
X_balanced, y_balanced = smote.fit_resample(X, y)

# Combine balanced numerical data with original categorical data
X_balanced = pd.DataFrame(X_balanced, columns=numerical_columns)
df_balanced = pd.concat([X_balanced, df[categorical_columns].reset_index(drop=True), pd.DataFrame(y_balanced, columns=['crime_type'])], axis=1)

# Convert date back to datetime
df_balanced['date'] = pd.to_datetime(df_balanced['date'], unit='s')

# Reorder the columns to match the desired order
df_balanced = df_balanced[columns]

# Save to CSV
df_balanced.to_csv('data.csv', index=False)

print("Data has been generated,and saved to 'balanced_data.csv'.")
