from helpers import create_seq, locate


def run_fib():
    data = input()
    sequence = []
    while not data == "Stop":
        split_data = data.split()
        number = int(split_data[-1])
        if split_data[0] == "Create":
            sequence = create_seq(number)
            print(*sequence)
        elif split_data[0] == "Locate":
            locate(sequence, number)
        data = input()