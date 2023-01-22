"""Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square that has maximal sum of its
elements. There will be no case with two of more 3x3 squares with equal maximal sum.
Input
•	On the first line, you will receive the rows and columns in format "{rows} {columns}" – integers in range [1, 20]
•	On the next lines you will receive each row with its columns - integers, separated by a single space
Output
•	On the first line print the maximum sum of the elements in the 3x3 square in format "Sum = {sum}"
•	On the next 3 lines print each element of the found submatrix, separated by a single space"""

import sys

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])


max_sum = -sys.maxsize
start_row = 0
start_col = 0

for row in range(rows-2):
    current_sum = 0
    for col in range(cols-2):
        # check each square and if all element in the square same count
        current_sum = matrix[row][col] +\
                     matrix[row][col+1] +\
                     matrix[row][col+2] +\
                     matrix[row+1][col] +\
                     matrix[row+1][col+1]+\
                     matrix[row+1][col+2]+\
                     matrix[row+2][col]+\
                     matrix[row+2][col+1]+\
                     matrix[row+2][col+2]

        if current_sum > max_sum:
            max_sum, start_row, start_col = current_sum, row, col


print(f"Sum = {max_sum}")

print(matrix[start_row][start_col], matrix[start_row][start_col+1], matrix[start_row][start_col+2])
print(matrix[start_row+1][start_col], matrix[start_row+1][start_col+1], matrix[start_row+1][start_col+2])
print(matrix[start_row+2][start_col], matrix[start_row+2][start_col+1], matrix[start_row+2][start_col+2])

