'''On the first line, you will receive a command - "Odd" or "Even". You will receive a sequence of numbers
(integers) on the second line, separated by a single space.
•	If the command is "Odd", print the sum of the odd numbers multiplied by the count of all numbers.
•	If the command is """"Even", print the sum of the even numbers multiplied by the count of all numbers.'''


command = input()
numbers = [int(x) for x in input().split()]
parity = 0
if command == "Odd":
    parity = 1

else:
    parity = 0

result = sum(filter(lambda x: (x % 2 == parity), numbers))
print(result * len(numbers))

