# Write a program which prints a set of elements. On the first line, you will receive two numbers - n and m,
# separated by a single space - they represent the lengths of two separate sets. On the next n + m lines you
# will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set.
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}



n = [int(x) for x in input().split()]
set_1 = set()
set_2 = set()
for _ in range(n[0]):
    number = int(input())
    set_1.add(number)

for _ in range(n[1]):
    number = int(input())
    set_2.add(number)

[print(x) for x in set_1 & set_2]