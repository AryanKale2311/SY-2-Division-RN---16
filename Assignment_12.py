
import numpy as np
import pandas as pd

data = {
    "Age": [25, 30, np.nan, 40, 35, 28],
    "Charges": [500, 600, 450, np.nan, 700, 550],
    "Churn": ["Yes", "No", "Yes", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Charges"] = df["Charges"].fillna(df["Charges"].mean())

print("\nCleaned Data:")
print(df)

print("\nSummary Statistics:")
print(df.describe())

print("\nChurn Analysis:")
churn = df["Churn"].value_counts()
print(churn)

print("\nAverage Charges:")
print(df.groupby("Churn")["Charges"].mean())

print("\nChurn Visualization:")

for name, count in churn.items():
    print(name, "*" * count)

print("\nAge Visualization:")

age = df["Age"].astype(int)

for value in sorted(age.unique()):
    count = sum(age == value)
    print(value, "*" * count)

