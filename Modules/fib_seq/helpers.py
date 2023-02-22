def create_seq(n):
    seq = [ 0, 1]

    for _ in range(3, n+1):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate(seq, num):
    if num in seq:
            print(f"The number {num} is at index {seq.index(num)}")
    else:
        print(f"The number {num} is not in the sequence")