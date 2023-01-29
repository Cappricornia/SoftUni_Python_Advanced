# Write a function called concatenate() that receives some strings, concatenates them, and returns the result.


def concatenate(*args):
    concat_string = ''
    for strg in args:
        concat_string += strg

    return concat_string


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
