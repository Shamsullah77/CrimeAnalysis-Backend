import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import pickle
from preprocess import clean_and_prepare_data

# Load the dataset
df = pd.read_csv('Crime_Data.csv')

# Preprocess the data
df_cleaned, category_mappings = clean_and_prepare_data(df)

# Features and target
X = df_cleaned.drop(columns=['crime_type'])
y = df_cleaned['crime_type']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model using Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Detailed classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save the model and the category mappings
with open('crime_model.pkl', 'wb') as file:
    pickle.dump((model, category_mappings), file)







# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# # from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# import pickle
# from preprocess import clean_and_prepare_data


# # Load the dataset
# df = pd.read_csv('Crime_Data.csv')

# # Preprocess the data
# df_cleaned = clean_and_prepare_data(df)

# # Features and target
# X = df_cleaned.drop(columns=['crime_type'])
# y = df_cleaned['crime_type']

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the model
# model = DecisionTreeClassifier(random_state=42)
# model.fit(X_train, y_train)

# # Save the model
# with open('crime_model.pkl', 'wb') as file:
#     pickle.dump(model, file)
