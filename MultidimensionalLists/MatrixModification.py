"""Write a program that reads a matrix from the console and changes its values. On the first line, you will get the
matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space.
You will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
indexes are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program."""

def is_not_valid(rows, cols, num):
    if rows < 0 or cols < 0 or rows >= num or cols >= num:
        return True

    return False


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()

    if line == "END":
        break

    command = line.split()[0]
    row, col, value = [int(x) for x in line.split()[1:]]

    if is_not_valid(row, col, n):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value

    elif command == "Subtract":
        matrix[row][col] -= value

for line in matrix:
    print(*line)
