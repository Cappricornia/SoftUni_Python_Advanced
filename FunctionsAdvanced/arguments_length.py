#Create a function called args_length() that returns the number of the arguments.
# Submit only the function in the judge system.


def args_length(*args):
    return len(args)


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
