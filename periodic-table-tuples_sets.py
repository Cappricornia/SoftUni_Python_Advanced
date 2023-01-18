# Write a program that keeps all the unique chemical elements. On the first line you will be given a number
# n - the count of input lines that you are going to receive. On the next n lines, you will be receiving chemical
# compounds, separated by a single space. Your task is to print all the unique ones on separate lines
# (the order does not matter):



n = int(input())
unique_elements = set()

for _ in range(n):
    chem_element = input().split()
    for el in chem_element:
        unique_elements.add(el)

[print(el) for el in unique_elements]