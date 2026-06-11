import pandas as pd
import pickle

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#Modul untuk evaluasi model
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Load dataset
df = pd.read_csv("student_stress_dataset_no_decimals.csv")
print(df.head())
numerical_cols = [
    "sleep_quality",
    "academic_performance",
    "study_load",
    "extracurricular_activity"
]

for col in numerical_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna()
#Feature
X = df[
    [
        "sleep_quality",
        "academic_performance",
        "study_load",
        "extracurricular_activity"
    ]
]

# Target
y = df["stress_level"]

# Encode label
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# Train model
model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Prediksi data testing
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n=== HASIL EVALUASI MODEL ===")
print(f"Accuracy: {accuracy:.2%}")

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
# Simpan model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

# Simpan encoder
with open("encoder.pkl", "wb") as file:
    pickle.dump(encoder, file)

print("Model berhasil dibuat!")