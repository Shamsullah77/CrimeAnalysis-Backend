import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

def genrate():
    # Define parameters
    num_records = 1000

    # Generate fake data
    data = {
        'date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
        'time': [fake.time() for _ in range(num_records)],
        'location': [fake.address() for _ in range(num_records)],
        'crime_type': [random.choice(['theft', 'assault', 'burglary', 'vandalism']) for _ in range(num_records)],
        'latitude': [fake.latitude() for _ in range(num_records)],
        'longitude': [fake.longitude() for _ in range(num_records)],
    }

    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)

    print(df.head())
genrate()