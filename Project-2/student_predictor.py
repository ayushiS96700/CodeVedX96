import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "student_data.csv")

df = pd.read_csv(csv_path)

print("Dataset")
print(df.head())

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataset Information")
print(df.info())

print("\nStatistics")
print(df.describe())

print("\nCorrelation Matrix")
print(df.corr())

plt.figure(figsize=(6,4))
plt.scatter(df["Study_Hours"], df["Final_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["Attendance"], bins=5)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.show()

X = df[[
    "Attendance",
    "Study_Hours",
    "Assignment",
    "Internal_Marks",
    "Previous_Marks"
]]

y = df["Final_Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

score = r2_score(y_test, prediction)

print("\nModel Accuracy (R² Score):", score)


print("\nEnter Student Details")

attendance = float(input("Attendance: "))
study = float(input("Study Hours: "))
assignment = float(input("Assignment Score: "))
internal = float(input("Internal Marks: "))
previous = float(input("Previous Marks: "))

student = [[
    attendance,
    study,
    assignment,
    internal,
    previous
]]

result = model.predict(student)

print("\nPredicted Final Marks:", round(result[0],2))

marks = result[0]

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Predicted Grade:", grade)
