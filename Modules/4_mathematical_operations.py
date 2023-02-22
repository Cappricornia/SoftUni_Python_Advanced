# data = input()
#
# print(f"{eval(data):.2f}") # will convert string to python code int and operator
# eval can't recognise ^ exponentiation (power)


# create package
# create package simple_operations
# in simple_operations create:
# file operation_functions.py write the functions
# file helper.py and create operation_mapper and import functions from operational_functions.py


from simple_operations.helper import operation_mapper
data = input().split()

a = float(data[0])
sign = data[1]
b = float(data[2])

"""the mapper using the key, has as a reference the name of the respective function, we give parameters a, b
which will be replaced from the input
the mapper goes to the __init__ file which is empty, then goes to helper.py, checking the functions and goes to the
operation_mapper which is a dictionary with a key string and reference to the respective function (it doesn't call
the function, just a reference)
once we get the reference to the function and call the function with a, b and replace with the numbers, the code
below will execute the respective function, depending on the operator"""
try:
    print(operation_mapper[sign](a, b))
except ZeroDivisionError:
    print("Invalid number b. b should not be 0 if divide")