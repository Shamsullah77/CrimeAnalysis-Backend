import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import uniform, randint
from imblearn.over_sampling import SMOTE

# Load preprocessed data
def load_preprocessed_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'preprocessed_data.pkl')
    X_preprocessed, y_crime_type, y_location = joblib.load(file_path)
    return X_preprocessed, y_crime_type, y_location

# Train and evaluate models
def train_and_evaluate(x_train, y_train, prams, model_name):
    RFC = RandomForestClassifier()
    rnd_search = RandomizedSearchCV(RFC, prams, n_iter=30, cv=3, n_jobs=-1, random_state=42)
    rndx = rnd_search.fit(x_train, y_train)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    joblib.dump(rndx, os.path.join(current_dir, f'final_random_forest_model_for_{model_name}.pkl'))
    return rndx

if __name__ == "__main__":
    X_preprocessed, y_crime_type, y_location = load_preprocessed_data()

    x_train, x_test, y_train, y_test = train_test_split(X_preprocessed, pd.DataFrame({'crime_type': y_crime_type, 'location': y_location}), test_size=0.2, random_state=42)

    smote = SMOTE(random_state=42)
    X_resampled_type, y_resampled_type = smote.fit_resample(x_train, y_train['crime_type'])
    X_resampled_location, y_resampled_location = smote.fit_resample(x_train, y_train['location'])

    prams = {
        "max_features": uniform(0.2, 0.8),
        "n_estimators": randint(2, 400),
        "max_depth": randint(2, 10),
        "min_samples_split": randint(2, 10)
    }

    rndx_type = train_and_evaluate(X_resampled_type, y_resampled_type, prams, "crime_type")
    rndx_location = train_and_evaluate(X_resampled_location, y_resampled_location, prams, "location")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    joblib.dump((x_test, y_test), os.path.join(current_dir, 'test_data.pkl'))
    print("Model training complete.")
