"""Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the
matrix's dimensions in format "{rows} {columns}". On the next rows you will receive characters, separated by a single
space. Print the number of all square matrices you have found."""

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

count = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            count += 1

print(count)