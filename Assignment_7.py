import re

text = "Contact us at abc@gmail.com or xyz123@yahoo.com"

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")

for email in emails:
    print(email)
