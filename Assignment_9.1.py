
f = open("data.txt", "r")

word = input("Enter word: ")
count = 0

for line in f:
    if word.lower() in line.lower():
        count += 1

f.close()

print("Number of lines:", count)
