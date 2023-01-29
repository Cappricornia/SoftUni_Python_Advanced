"""You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers
from the positive. Find the total sum of the negatives and positives, and print the following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
o	If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
o	If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input."""


def sum_negative_positive(nums):
    positive = 0
    negative = 0
    for n in nums:
        if n > 0:
            positive += n
        else:
            negative += n

    if abs(positive) > abs(negative):
        return f"{negative}\n{positive}\nThe positives are stronger than the negatives"
    else:
        return f"{negative}\n{positive}\nThe negatives are stronger than the positives"


line = [int(x) for x in input().split()]
print(sum_negative_positive(line))


