from operation_functions import sum_nums, sub_nums, div_nums, mul_nums, pow_nums

# create mapper to avoid if/elif statements use the operator as a key and name func as a reference
operation_mapper = {
    "+": sum_nums,
    "-": sub_nums,
    "/": div_nums,
    "*": mul_nums,
    "^": pow_nums

}


# another option is to create a function with eval
'''
def calculate(sign, a ,b):
    if sign in ("+", "-", "/", "*"):
        return eval(f"{a} {sign} {b}")
    if sign == "^":
        return a ** b    # "^" doesn't work with eval so we need to do it separately
    else:
        raise ValueError("Sign is not defined")
    
'''