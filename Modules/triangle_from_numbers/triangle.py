def print_up_part(n):
    for row_num in range(1, n+1):
        for num in range(1, row_num + 1):
            print(num, end="")
        print()


def print_bottom(n):
    for row_number in range(n-1, 0, -1):
        for number in range(1, row_number + 1):
            print(number, end="")
        print()


def print_triangle(n):
    print_up_part(n)
    print_bottom(n)


