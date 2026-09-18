import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from feature_extractor import extract_url_features


data = pd.read_csv("dataset.csv")

X = []
y = []

for _, row in data.iterrows():

    url = row["url"]
    label = row["label"]

    X.append(extract_url_features(url))
    y.append(label)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
print()
print(classification_report(y_test, predictions))


joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")