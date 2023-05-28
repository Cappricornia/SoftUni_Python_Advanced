# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing groups
# in your regular expression.
# Compose the Regular Expression
# Every valid date has the following characteristics:
# •	Always starts with two digits, followed by a separator
# •	After that, it has one uppercase and two lowercase letters (e.g. Jan, Mar).
# •	After that, it has a separator and exactly 4 digits (for the year).
# •	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward slash ("/").
# •	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a
# group backreference to check for this.
# You can follow the table below to help with composing your RegEx:

import re
pattern = r"\b(\d{2})(/|\.|-)([A-Z][a-z]{2})(\2)(\d{4})\b"
dates = input()
matches = re.finditer(pattern, dates)
for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(5)
    print(f"Day: {day}, Month: {month}, Year: {year}")
