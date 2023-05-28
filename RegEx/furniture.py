# Write a program which calculates the total cost of bought furniture. You will be given information about each
# purchase on separate lines until you receive the command "Purchase". Valid information should be in the format:
# ">>{furniture_name}<<{price}!{quantity}". The price could be floating-point or integer number. You should store
# the names of the furniture and the total price.
# At the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"


import re

furniture = input()
bought_furniture = []
total_price = 0
while not furniture == "Purchase":
    matches = re.finditer(r">>([A-Za-z]+)<<(\d+[\.\d+]*)!(\d+)", furniture)
    for match in matches:
        total_price += float(match.group(2)) * int(match.group(3))
        bought_furniture.append(match.group(1))
    furniture = input()

print(f"Bought furniture:")
if bought_furniture:
    print('\n'.join(bought_furniture))
print(f"Total money spend: {total_price:.2f}")



