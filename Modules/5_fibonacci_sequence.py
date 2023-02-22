# a solution before using modules
'''
def create_seq(n):
    seq = [ 0, 1]  # always have 0, 1 first two numbers

    for _ in range(3, n+1):
        seq.append(seq[-1] + seq[-2])
    return seq


data = input()
sequence = []
while not data == "Stop":
    split_data = data.split()
    number = int(split_data[-1])
    if split_data[0] == "Create":
        sequence = create_seq(number)
        print(*sequence)
    elif split_data[0] == "Locate":
        if number in sequence:
            print(f"The number {number} is at index {sequence.index(number)}")
        else:
            print(f"The number {number} is not in the sequence")

    data = input()


'''
# call the function run_fib in core.py
from fib_seq.core import run_fib

run_fib()


