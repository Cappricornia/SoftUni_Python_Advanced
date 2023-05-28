# Write a program which receives series of strings on different lines and extracts only the numbers. Print all
# extracted numbers on a single line, separated by a single space.


import re

line_input = input()
pattern = r"\d+"
list_of_nums = []

while line_input:
    matches = re.findall(pattern, line_input)
    list_of_nums.extend(matches)

    line_input = input()

print(*list_of_nums)

