f = open("input.txt", "r")

lines = f.readlines()

print("Total lines:", len(lines))

f.close()

f = open("output.txt", "w")

f.writelines(lines[:2])

f.close()

print("First two lines copied successfully")
