# On a circle road there are N petrol pumps. Petrol pumps are numbered 0 to (N−1) (both inclusive). For each petrol
# pump you will receive two pieces of information:
# -	the amount of petrol that petrol pump will give
# -	the distance from that petrol pump to the next petrol pump (kilometers)
# Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps.
# Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop
# at each of the petrol pumps. The truck will move one kilometer for each liter of the petrol.
# Input
# •	On the first line you will receive the N-number petrol pumps
# •	On the next N-lines you will receive the amount of petrol that petrol pump will give and the distance between that
# petrol pump and the next petrol pump, separated by single space
# Output
# •	An integer which will be the smallest index of the petrol pump from which you can start the tour
# Constraints
# •	1 ≤ N ≤ 1000001
# •	1 ≤ Amount of petrol, Distance ≤ 1000000000

from collections import deque
petrol_st = int(input())
queue = deque()

for _ in range(petrol_st):
    petrol_st = [int(x) for x in input().split()]
    queue.append(petrol_st)

for attempt in range(petrol_st):
    fuel = 0
    is_completed = True
    for petrol, distance in queue:
        fuel += petrol
        if distance > fuel:
            is_completed = False
            break
        fuel -= distance
    if is_completed:
        print(attempt)
        break
    queue.append(queue.popleft())




