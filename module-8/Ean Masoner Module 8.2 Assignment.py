import json

# Load the JSON data
with open('student.json', 'r') as file:
    student_data = json.load(file)
    print("Original Student List:")
    print(student_data)  # Debugging: print the loaded data to check if it's correct

    # Print each student's details in the desired format
    for student in student_data:
        print(f"Name: {student.get('f_name')} {student.get('l_name')}")
        print(f"ID: {student.get('Student_id', 'N/A')}, Email: {student.get('email', 'Not Available')}")
        print("-" * 21)  # This will print a separator line

# Add a new student
new_student = {
    "f_name": "Ean",
    "l_name": "Masoner",
    "Student_id": 1234,
    "email": "ean@example.com"
}
student_data.append(new_student)

# Print the updated student list
print("\nUpdated Student List:")
for student in student_data:
    print(f"Name: {student.get('f_name')} {student.get('l_name')}")
    print(f"ID: {student.get('Student_id', 'N/A')}, Email: {student.get('email', 'Not Available')}")
    print("-" * 21)  # This will print a separator line

# Save the updated list back to the JSON file
with open('student.json', 'w') as file:
    json.dump(student_data, file, indent=4)

print("\nStudent list has been updated and saved to the JSON file.")
