# Write a program that processes information about a race. On the first line you will be given list of
# participants separated by ", ". On the next few lines until you receive a line "end of race"
# you will be given some info which will be some alphanumeric characters. In between them you could have some
# extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e". The letters are the name of
# the person and the sum of the digits is the distance he ran. So here we have George who ran 29 km.
# Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance. At the end print
# the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"


import re

pattern_name = r"[a-zA-Z]"
pattern_nums = r"\d"
names = [name.strip() for name in input().split(",")]
race = input()
name_distance = {}
while not race == "end of race":
    result_name = re.findall(pattern_name, race)
    result_digit = [int(num) for num in re.findall(pattern_nums, race)]
    name = "".join(result_name)
    distance = sum(result_digit)

    if name in names:
        if name not in name_distance:
            name_distance[name] = distance
        else:
            name_distance[name] += distance

    race = input()

sorted_names_km = sorted(name_distance.items(), key=lambda x: -x[1])
print(f"1st place: {sorted_names_km[0][0]}")
print(f"2nd place: {sorted_names_km[1][0]}")
print(f"3rd place: {sorted_names_km[2][0]}")


