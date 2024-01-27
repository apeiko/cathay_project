wrongGrades = [35, 46, 57, 91, 29]

# List to store the fixed grades
fixedGrades = []

for i in wrongGrades:
    # Extract the tens and ones digits
    a = i // 10
    b = i % 10
    # Swap the tens and ones digits to get the correct grade
    correctGrades = b * 10 + a

    # Append the corrected grade to the list
    fixedGrades.append(correctGrades)

print("Grade before correction:", wrongGrades)
print("Grade after correction:", fixedGrades)