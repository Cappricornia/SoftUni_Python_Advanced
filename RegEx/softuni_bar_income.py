# Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to
# go home and you are the person who has to draw the line and calculate the money from the products that were
# sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input.
# But before processing that line you should do some validations first.
# Each valid order should have a customer, product, count and a price:
# •	Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case
# letters
# •	Valid product contains any word character (not only letters) and must be surrounded by '<' and '>'
# •	Valid count is an integer, surrounded by '|'
# •	Valid price is any real number followed by '$'
# The parts of a valid order should appear in the order given: customer, product, count and a price.
# Between each part there can be other symbols, except ('|', '$', '%' and '.')
# For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
# When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places
# in the following format: "Total income: {income}".


import re

pattern = r"^%([A-Z][a-z]+)%.*<(\w+)>.*\|(\d+)\|\D*(\d+\.?\d+)\$$"
customers = input()
valid_customers = []
total_income = 0
while not customers == "end of shift":
    matches = re.finditer(pattern, customers)
    for match in matches:
        name = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))
        valid_customers.append([name, product, count, price])
    customers = input()

for customer in valid_customers:
    total_price = customer[2] * customer[3]
    total_income += total_price
    print(f"{customer[0]}: {customer[1]} - {total_price:.2f}")
print(f"Total income: {total_income:.2f}")

