'''
Create a function called func_executor() that can receive a different number of tuples,
each of which will have exactly 2 elements: first will be a function, and the second will be a tuple of the
arguments that need to be passed to that function.
Create a list that will contain all the results of the executed
functions with their corresponding arguments and return it after executing all functions. For more clarification,
see the examples below. Submit only your function in the judge system.'''


def f_executor(*args):
    result = []
    for func, func_args in args: # tuples
        result.append(func(*func_args))

    return result


def sum_nums(num1, num2):
    return num1 + num2


def multiply_nums(num1, num2):
    return num1 * num2


print(f_executor((sum_nums, (1, 2)), (multiply_nums, (2, 4))))