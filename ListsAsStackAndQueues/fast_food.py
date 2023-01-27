# You have a fast-food restaurant and most of the food that you are offering is previously prepared. You need to know
# if you will have enough food to serve lunch to all your customers.
# Write a program which checks the orders' quantity. You also want to know who the client with the biggest order for
# that day is, because you want to give him a discount.
# First, you will be given the quantity of the food that you have for the day (an integer number). Next, you will be
# given a sequence of integers, each representing the quantity of an order. Keep the orders in a queue.
# Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came.
# Before each order, check if you have enough food left to complete it. If you have, remove the order from the
# queue and reduce the amount of food you have. Otherwise, stop serving.
# Input
# •	On the first line you will be given the quantity of your food - an integer in the range [0, 1000]
# •	On the second line you will receive a sequence of integers, representing each order, separated by a single space
# Output
# •	On the first line, print the quantity of biggest order
# •	If you succeeded in servicing all your clients, print: "Orders complete".
# •	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
# Constraints
# •	The input will always be valid

from collections import deque
total_food = int(input())
orders = deque(map(int, input().split()))
max_order = max(orders)
print(max_order)
while orders:
    curr_order = orders[0]
    if curr_order > total_food:
        break
    else:
        total_food -= curr_order
        orders.popleft()
if orders:
   print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")