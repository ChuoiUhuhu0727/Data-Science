# Print a dictionary 
# of students' names & scores
student_scores = {
    "Bong": 90, 
    "Hoa": 85,
    "Mai": 78
}

for student, score in student_scores.items():
  print(f"{student}: {score}")

# Create a dictionary with a key (a number) 
# and a value (the square of that number)
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

# Print positions & Values
# of a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    print(f"Position: ({i}, {j}), Value: {matrix[i][j]}")

