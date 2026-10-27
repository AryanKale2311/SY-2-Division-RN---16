with open("input.txt", "r") as f:
    lines = f.readlines()
print("Total lines:", len(lines))
first_two = lines[:2]
with open("output.txt", "w") as f:
    f.writelines(first_two)
