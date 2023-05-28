# Plant Discovery

# You have now returned from your world tour. On your way, you have discovered some new plants, and you want to gather
# some information about them and create an exhibition to see which plant is highest rated.
# On the first line, you will receive a number n. On the next n lines, you will be given some information about the
# plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need
# it later. If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given command is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The plants should be sorted by rarity in descending order. If two or more plants have the same rarity value sort
# them by average rating in descending order. The average rating should be formatted to the second decimal place.
# Input / Constraints
# •	You will receive the input as described above
# Output
# •	Print the information about all plants as described above

number = int(input())
plants = {}
for _ in range(number):
    info_plant = input().split("<->")
    plant_name = info_plant[0]
    rarity = int(info_plant[1])
    plants[plant_name] = {"rarity": rarity, "ratings": []}

command = input().split(": ")
while not command[0] == "Exhibition":
    data = command[1].split(" - ")
    plant = data[0]

    try:

        if command[0] == "Rate":
            rating = int(data[1])
            plants[plant]["ratings"].append(rating)
        elif command[0] == "Update":
            new_rarity = int(data[1])
            plants[plant]["rarity"] = new_rarity
        elif command[0] == "Reset":
            plants[plant]["ratings"].clear()
        else:
            print("error")

    except KeyError:
        print("error")

    command = input().split(": ")


for plant_name, value in plants.items():
    if value["ratings"]:
        avg_rating = sum(value["ratings"]) / len(value["ratings"])
    else:
        avg_rating = 0
    plants[plant_name]["average"] = avg_rating

    #Ex. {'Candelabra': {'rarity': 10, 'ratings': [6], 'average': 6.0}, 'Oahu': {'rarity': 10, 'ratings': [7], 'average': 7.0}}

sorted_plants = sorted(plants.items(), key=lambda tkvp: (-tkvp[1]['rarity'], -tkvp[1]['average']))

# [('Oahu', {'rarity': 10, 'ratings': [7], 'average': 7.0}), ('Candelabra', {'rarity': 10, 'ratings': [6], 'average': 6.0})]

print("Plants for the exhibition:")

for plant, value in sorted_plants:
    print(f"- {plant}; Rarity: {value['rarity']}; Rating: {value['average']:.2f}")

