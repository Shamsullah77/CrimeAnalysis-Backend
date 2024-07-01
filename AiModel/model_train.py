# import pandas as pd
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, accuracy_score
# import joblib

# def train_model(data_path, model_output_path):
#     # Load the processed dataset
#     df = pd.read_csv('cleaned_data.csv')
    
#     # Define the target variable and features
#     X = df.drop(columns=['location'])
#     y = df['location']
    
#     # Split the data into training and testing sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#     # Initialize the Random Forest Classifier
#     rf_clf = RandomForestClassifier(random_state=42)
    
#     # Define the parameter grid for GridSearchCV
#     param_grid = {
#         'n_estimators': [3,4,6,10,30,60],
#         'max_features':[2,6,8,15,30]
#     }
    
#     # Initialize GridSearchCV
#     grid_search = GridSearchCV(estimator=rf_clf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
    
#     # Fit the model
#     grid_search.fit(X_train, y_train)
    
#     # Get the best model
#     best_rf_clf = grid_search.best_estimator_
    
#     # Make predictions
#     y_pred = best_rf_clf.predict(X_test)
#     y_pred_prob = best_rf_clf.predict_proba(X_test)
    
#     # Print classification report and accuracy
#     print("Classification Report:\n", classification_report(y_test, y_pred))
#     print("Accuracy:", accuracy_score(y_test, y_pred))
    
#     # Save the model
#     joblib.dump(best_rf_clf, model_output_path)
#     print(f"Model saved to {model_output_path}")
    
#     return best_rf_clf, X_test, y_test, y_pred, y_pred_prob

# if __name__ == "__main__":
#     data_path = 'cleaned_data.csv'
#     model_output_path = 'crime_location_model.pkl'
#     model, X_test, y_test, y_pred, y_pred_prob = train_model(data_path, model_output_path)
    
#     # Example usage
#     print("\nExample predictions:")
#     for i in range(5):
#         print(f"Actual: {y_test.iloc[i]}, Predicted: {y_pred[i]}, Probability: {y_pred_prob[i]}")




import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import warnings

def train_model(data_path, model_output_path):
    # Suppress warnings
    warnings.filterwarnings("ignore")
    
    # Load the processed dataset
    df = pd.read_csv('cleaned_data.csv')
    
    # Print columns used for training
    features = df.drop(columns=['crime_type', 'location']).columns
    print("Features used for training:")
    for feature in features:
        print(feature)
    print()
    
    # Define the target variables and features
    X = df.drop(columns=['crime_type', 'location'])  # Features
    y = df[['crime_type', 'location']]  # Targets
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the base Decision Tree Classifier
    dt_clf = DecisionTreeClassifier(random_state=42)
    
    # Wrap the Decision Tree Classifier in MultiOutputClassifier for multi-output prediction
    multi_output_clf = MultiOutputClassifier(dt_clf)
    
    # Define the parameter grid for GridSearchCV
    param_grid = {
        'estimator__max_depth': [10, 20, 30],  # Reduce range for quicker execution
        'estimator__min_samples_split': [2, 5, 10],
        'estimator__min_samples_leaf': [1, 2, 4],
        'estimator__criterion': ['gini', 'entropy']
    }
    
    # Initialize GridSearchCV
    grid_search = GridSearchCV(estimator=multi_output_clf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=0)  # Set verbose to 0
    
    # Fit the model
    grid_search.fit(X_train, y_train)
    
    # Get the best model
    best_clf = grid_search.best_estimator_
    
    # Make predictions
    y_pred = best_clf.predict(X_test)
    
    # Print classification reports and accuracies for crime type and location
    for i, target_name in enumerate(['crime_type', 'location']):
        print(f"Classification Report for {target_name}:\n", classification_report(y_test[target_name], y_pred[:, i]))
        print(f"Accuracy for {target_name}:", accuracy_score(y_test[target_name], y_pred[:, i]))
        print()
    
    # Print best parameters found by GridSearchCV
    print("Best Parameters:", grid_search.best_params_)
    
    # Save the model
    joblib.dump(best_clf, model_output_path)
    print(f"Model saved to {model_output_path}")
    
    return best_clf, X_test, y_test, y_pred

if __name__ == "__main__":
    data_path = 'cleaned_data.csv'
    model_output_path = 'crime_model_dt.pkl'
    model, X_test, y_test, y_pred = train_model(data_path, model_output_path)
    
    # Example usage
    print("\nExample predictions:")
    for i in range(5):
        print(f"Actual Crime Type: {y_test['crime_type'].iloc[i]}, Predicted Crime Type: {y_pred[i][0]}")
        print(f"Actual Location: {y_test['location'].iloc[i]}, Predicted Location: {y_pred[i][1]}")
        print()
