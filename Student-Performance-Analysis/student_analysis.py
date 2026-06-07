import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nStudent Performance Summary")
print(df)

topper = df.loc[df["Average"].idxmax()]

print("\nTop Performer:")
print(topper["Name"])

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()