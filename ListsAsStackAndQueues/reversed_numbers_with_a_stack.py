# Write a program that reads from the console a string with N integers, separated by a single space,
# and reverses them using a stack. Print the reversed integers on one line, separated by a single space.

sequence_nums = input().split()
reversed_nums = []
while sequence_nums:
      reversed_nums.append(sequence_nums.pop())
print(' '.join(reversed_nums))
