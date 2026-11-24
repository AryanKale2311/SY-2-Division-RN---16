
import csv

with open("employee.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Monthly Salary"])
    w.writerow(["Aryan", 60000])
    w.writerow(["Rahul", 40000])
    w.writerow(["Amit", 55000])

with open("employee.csv", "r") as f:
    r = csv.DictReader(f)

    for row in r:
        name = row["Name"]
        salary = int(row["Monthly Salary"])
        annual = salary * 12

        print("Name:", name)
        print("Annual Salary:", annual)

        if salary > 50000:
            print("Above 50000")
        print()
