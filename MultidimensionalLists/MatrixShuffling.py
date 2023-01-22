"""Write a program that reads a matrix, from the console and perform certain operations with its elements. User input
is provided in a similar way like in the problems above - first you read the dimensions and then the data.
Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and
("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword
along with four valid coordinates (no more, no less), separated by a single space.
•	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus
you will be able to check if the operation was performed correctly).
•	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered or the
given coordinates are not valid), print "Invalid input!" and move on to the next command. A negative value makes
the coordinates not valid.
Your program should finish when the command "END" is entered."""



rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    line = input()
    if line == "END":
        break

    command = line.split()

     # This line will be executed only if m is true and 4 indices but won't check for valid indices
    #If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
    # or the given coordinates are not valid move on to the following command

    if not command[0] == "swap" or not len(command) == 5:
        print("Invalid input!")
        continue

    row_1, col_1, row_2, col_2 = [int(x) for x in command[1:]]

    #or the given coordinates are not valid and move on to the following command.
    # A negative value makes the coordinates not valid.

    if row_1 < 0 or col_1 < 0 or row_2 < 0 or col_2 < 0 or row_1 >= rows or row_2 >= rows or col_1 >= cols or\
            col_2 >= cols:
        print("Invalid input!")
        continue

    # swapping makes tuples that is unpacked in the variables
    # a, b = 3, 4
    # a, b = b, a -> tuple of b, a , 4, 3 and assign the value a= 4, b=3
    matrix[row_1][col_1],  matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

    # print matrix on each iteration
    for row_el in matrix:
        print(' '.join([x for x in row_el]))






