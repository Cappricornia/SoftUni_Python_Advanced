"""You will be given a sequence of integers – each indicating a cup's capacity (in litters). After that, you will be
given another sequence of integers – each indicating a bottle's capacity (in litters). Your job is to try to fill up
all the cups.
You must start picking from the last received bottle and start filling from the first entered cup. You could pick
exactly one bottle at a time. If the current bottle has N water, you give the first entered cup N water and reduce
its integer value by N.
When a cup's integer value reaches 0 or less, it gets removed. It is possible that the current cup's value is greater
than the current bottle's value. In that case, you pick bottles until you reduce the cup's integer value to 0 or less.
If a bottle's value is greater or equal to the cup's current value, you fill up the cup, and the remaining water
becomes wasted. You should keep track of the wasted litters of water and print them at the end of the program.
If you have managed to fill up all the cups, print the remaining water bottles, from the last entered – to the first.
Otherwise, you must print the remaining cups ordered by the entrance – from the first entered – to the last.
Input
•	On the first line of input, you will receive the integers representing the cups' capacity,
separated by a single space.
•	On the second line of input, you will receive the integers representing the filled bottles,
separated by a single space.
Output
•	On the first line:
o	If you filled all the cups, print the remaining bottles as specified:
"Bottles: {bottle1} {bottle2} ... {bottleN}"
o	If you used all the bottles of water, print the remaining cups as specified:
"Cups: {cup1} {cup2} ... {cupN}"
•	On the second line, print the wasted litters of water in the following format:
"Wasted litters of water: {wasted_litters_of_water}."
Constraints
•	All the given numbers will be valid integers in the range [1, 1000].
•	It is safe to assume that there will be NO case in which the water is exactly as much as the cups'
values so that in the end, there are no cups and no water in the bottles.
•	There will be NO case where a cup will be almost full at the end."""


from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups and bottles:
    current_cup = cups[0]
    while current_cup > 0:
        current_bottle = bottles.pop()
        current_cup -= current_bottle
    wasted_water -= current_cup
    cups.popleft()

if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {wasted_water}")





