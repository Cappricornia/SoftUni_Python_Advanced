"""Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}"."""

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary = []
secondary = []
for row in range(n):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][n - 1 - row])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")

print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")