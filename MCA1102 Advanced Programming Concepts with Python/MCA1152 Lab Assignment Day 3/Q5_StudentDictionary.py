# 5. Given a dictionary that contains a student’s roll, name and a list of marks, 

# (i) 
# Update the dictionary with an added item of the total of the student’s marks. 
# Sample 
# Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]} 
# Output: {'roll': 5, 'Name': 'Ananya', 'marks': [79, 88, 92], 'total': 259} 

# (ii) 
# Update the dictionary with an added entry of the total of the student’s marks in the list. 
# Sample 
# Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]} 
# Output: {'roll': 5, 'Name': 'Ananya', 'marks': [79, 88, 92, 259]} 

# (iii) Update the dictionary with the students’ marks list replaced by the total marks of the 
# student. 
# Sample 
# Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]} 
# Output: {'roll': 5, 'Name': 'Ananya', 'marks': 259} 

# dictionary that contains a student’s roll, name and a list of marks, 
student = {
    "Name": "SUMANTA BHATTACHARYA",
    "roll_no": 2682005,
    "marks": [52.6, 69.8, 75.9]
}

# (i) 
# Update the dictionary with an added item of the total of the student’s marks. 
# Sample 
# Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]} 
# Output: {'roll': 5, 'Name': 'Ananya', 'marks': [79, 88, 92], 'total': 259} 

totalMarks = sum(student["marks"])

student["totalMarks"] = totalMarks

print(student)

# (ii) 
# Update the dictionary with an added entry of the total of the student’s marks in the list. 
# Sample 
# Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]} 
# Output: {'roll': 5, 'Name': 'Ananya', 'marks': [79, 88, 92, 259]} 

student["marks"].append(totalMarks)

print(student)

# (iii) Update the dictionary with the students’ marks list replaced by the total marks of the 
# student. 
# Sample 
# Input: {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]} 
# Output: {'roll': 5, 'Name': 'Ananya', 'marks': 259} 

student["marks"] = totalMarks
print(student)