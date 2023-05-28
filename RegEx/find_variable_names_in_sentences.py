# Write a program which finds all variable names in each string. A variable name starts with an underscore ("_")
# and contains only capital and non-capital letters and digits. Extract only their names, without the underscore.
# Try to do this only with regular expressions.
# The output consists of all variable names, extracted, and printed on a single line, separated by a comma.

import re
text = input()
match = [variable[2] for variable in re.finditer(r"\b(_)([a-zA-Z0-9]+)\b", text)]
print(*match, sep=',')
