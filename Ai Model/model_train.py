from preprocess import Data_preprocesser
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import pandas as pd

df = pd.read_csv('C:/Users/Shamsullah/Desktop/Ai Model/Crime_Data.csv')

df = Data_preprocesser(df)
# Define features and target
X = df.drop(columns=['crime_type'])
y = df['crime_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)


# Assuming 'model' is your trained model
with open('crime_model.pkl', 'wb') as file:
    pickle.dump(model, file)
