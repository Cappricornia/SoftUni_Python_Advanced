# You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of
# each letter in the name and integer divide it to the number of the current row (starting from 1). Save the result
# to a set of either odd or even numbers, depending on if the devised number is an odd or even. After that, sum the
# values of each set.
# •	If the sums of the two sets are equal, print the union of the values, separated by ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated
# by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different values,
# separated by ", ".
# NOTE: On every operation, the starting set should be the odd set


n = int(input())
odd_nums = set()
even_nums = set()

for num in range(1, n + 1):
    name = input()
    sum_name = 0
    for letter in name:
        sum_name += ord(letter)
    sum_name //= num
    if sum_name % 2 == 0:
        even_nums.add(sum_name)
    else:
        odd_nums.add(sum_name)

even_sum = sum(even_nums)
odd_sum = sum(odd_nums)
result = set()
if even_sum == odd_sum:
    result = odd_nums.union(even_nums)
elif odd_sum > even_sum:
    result = odd_nums.difference(even_nums)
else:
    result = odd_nums.symmetric_difference(even_nums)
print(", ".join([str(x) for x in result]))
