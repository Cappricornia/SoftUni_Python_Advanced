#  P!rates

# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels.
# Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and
# treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the
# pirate's way!
# Until the "Sail" command is given, you will be receiving:
# •	You and your crew have targeted cities, with their population and gold, separated by "||".
# •	If you receive a city that has already been received, you have to increase the population and gold with the
# given values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town, killing the given number of people and stealing the
# respective amount of gold.
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message: "{town} has been
# wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added
# cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the
# following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
# •	On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their
# gold and population, separated by "||"
# •	On the following lines, until the "End" command, you will be receiving strings representing the actions described
# above, separated by "=>"
# Output
# •	After receiving the "End" command, if there are any existing settlements on your list of targets, you need to
# print all of them, sorted by their gold in descending order, then by their name in ascending order, in the
# following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg"
# •	If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"
# Constraints
# •	The initial population and gold of the settlements will be valid 32-bit integers, never negative, or
# exceed the respective limits.
# •	The town names in the events will always be valid towns that should be on your list.

data = input()

cities = {}

while not data == "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)

    if city not in cities.keys():
        cities[city] = []
        cities[city] = [population, gold]

    else:
        data_city = cities[city]
        data_city[0] += population
        data_city[1] += gold

    data = input()

while True:
    command = input()

    if command == "End":
        break

    event = command.split("=>")
    town = event[1]

    if event[0] == "Plunder":
        people = int(event[2])
        gold_stolen = int(event[3])
        town_data = cities[town]
        town_data[0] -= people
        town_data[1] -= gold_stolen
        print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")

        if town_data[0] == 0 or town_data[1] == 0:
            print(f"{town} has been wiped off the map!")
            cities.pop(town)

    elif event[0] == "Prosper":
        gold_to_add = int(event[2])
        town_treasury = cities[town]

        if gold_to_add < 0:
            print("Gold added cannot be a negative number!")
            continue

        town_treasury[1] += gold_to_add
        print(f"{gold_to_add} gold added to the city treasury. {town} now has {town_treasury[1]} gold.")

if len(cities.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    for key, value in sorted(cities.items(), key=lambda x: (-x[1][1], x[0])):
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")



