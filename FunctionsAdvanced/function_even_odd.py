'''Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
Submit only the function in the judge system.'''


def even_odd(*args):
    numbers = [int(x) for x in args[:-1]]
    command = args[-1]
    parity = 0 if command == "even" else 1
    result = list(filter(lambda x: (x % 2 == parity), numbers))
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))