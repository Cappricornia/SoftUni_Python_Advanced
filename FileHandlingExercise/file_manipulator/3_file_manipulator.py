from os import path, remove

while True:
    line_input = input()
    if line_input == "End":
        break
    line_args = line_input.split("-")
    command = line_args[0]
    file_name = line_args[1]

    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        content = line_args[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")
    elif command == "Replace":
        old_string = line_args[2]
        new_string = line_args[3]

        if not path.exists(file_name):
            print("An error occurred")
            continue

        with open(file_name, "r+") as file:
            new_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(new_content)
    else:
        if path.exists(file_name):
            remove(file_name)
        else:
            print("An error occurred")