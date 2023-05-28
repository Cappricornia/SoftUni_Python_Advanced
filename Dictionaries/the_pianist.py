#  The Pianist

# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help
# you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following
# format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|",
# until the "Stop" command is given:
# •	"Add|{piece}|{composer}|{key}":
# 	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# 	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# 	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# 	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# 	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# 	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection, sorted by their
# name and by the name of their composer in alphabetical order, in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.


number = int(input())
pieces = {}
for _ in range(number):
    piece, comp, k = input().split("|")
    pieces[piece] = {'composer': comp, 'music_key': k}

line = input()
while not line == "Stop":

    command = line.split("|")
    new_piece = command[1]

    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if new_piece in pieces:
            print(f"{new_piece} is already in the collection!")
        else:
            pieces[new_piece] = {'composer': composer, 'music_key': key}
            print(f"{new_piece} by {composer} in {key} added to the collection!")

    elif command[0] == "Remove":
        if new_piece in pieces:
            del pieces[new_piece]
            print(f"Successfully removed {new_piece}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        new_key = command[2]
        if new_piece in pieces:
            pieces[new_piece]['music_key'] = new_key
            print(f"Changed the key of {new_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")

    line = input()

sorted_pieces = sorted(pieces.items(), key=lambda tkvp: tkvp[0])

for piece, value in sorted_pieces:
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['music_key']}")
