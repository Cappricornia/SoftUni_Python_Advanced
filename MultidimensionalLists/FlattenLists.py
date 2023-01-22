"""Write a program to flatten several lists of numbers received in the following format:
	String with numbers or empty strings separated by "|"
	Values are separated by spaces (" ", one or several)
	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown
 below"""



line = input().split("|")

flatten_list = []

for index in range(len(line) -1, -1, -1):
    elements = line[index].split()
    flatten_list += elements

print(*flatten_list)