from string import punctuation

with open("text.txt", "r") as file_input, open("output.txt", "w") as file_output:
    for row, element in enumerate(file_input):
        letters = len([ch for ch in element if ch.isalpha()])
        punctual_marks = len([mark for mark in element if mark in punctuation])
        file_output.write(f"Line {row + 1}: {element.strip()} ({letters})({punctual_marks})\n")