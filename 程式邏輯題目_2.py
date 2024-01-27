resultList = {}

# Initialize counts for digits 0-9
for i in range(48, 58):
    resultList.update({chr(i): 0})
# Initialize counts for uppercase letters A-Z
for i in range(65, 91):
    resultList.update({chr(i): 0})

words = "Hello welcome to Cathay 60th year anniversary"

# Go through each character in the text
for i in words.upper():
    # Skip spaces
    if i == " ":
        continue
    # Update the count for the current character
    resultList[i] += 1
# Output the count for each letter or digit
for key, value in resultList.items():
    print(f"{key} {value}")