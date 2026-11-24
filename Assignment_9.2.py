
import csv
import json

with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Roll", "Name", "Branch", "Marks"])
    w.writerow([1, "Aryan", "CSE", 450])
    w.writerow([2, "Rahul", "IT", 380])
    w.writerow([3, "Amit", "CSE", 320])

students = []

with open("students.csv", "r") as f:
    r = csv.DictReader(f)

    for row in r:
        total = int(row["Marks"])
        percentage = total / 5

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        row["Total"] = total
        row["Percentage"] = percentage
        row["Grade"] = grade

        students.append(row)

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("Student records saved in JSON")
