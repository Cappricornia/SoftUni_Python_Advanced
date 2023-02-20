# KeyError  handling - Dictionary

dict = {"a": 1, "b": 2}

key = input()

while True:
    try:
        print(dict[key])
        break
    except KeyError:
        print("Invalid index. Please try again")
        key = input()
