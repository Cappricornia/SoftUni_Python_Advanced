"""Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. The next N lines holds the values
for each column - N numbers separated by a single space. Print the absolute difference between the sums of the
primary and the secondary diagonal."""



n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for index in range(n):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][n-1-index])

sum_primary = sum(primary_diagonal)
sum_secondary = sum(secondary_diagonal)

#difference abs(primary - secondary)
print(abs(sum_primary - sum_secondary))


