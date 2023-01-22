# Write a program which finds the longest intersection. You will be given a number N. On each of the next N lines
# you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should
# find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and
# its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length
# {length_longest_intersection}"
# Note: in each range, there will always be intersection. If there are two equal intersections, print the first one.



n = int(input())
longest_intersection = set()

for _ in range(n):
    set_1 = set()
    set_2 = set()
    data = input().split('-')
    first_start, first_end = [int(x) for x in data[0].split(',')]
    second_start, second_end = [int(x) for x in data[1].split(',')]
    for num in range(first_start, first_end + 1):
        set_1.add(num)
    for num in range(second_start, second_end + 1):
        set_2.add(num)

    current_set = (set_1 & set_2) # intersection or set_1.intersection(set_2)
    if len(current_set) > len(longest_intersection):
        longest_intersection = current_set

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")
