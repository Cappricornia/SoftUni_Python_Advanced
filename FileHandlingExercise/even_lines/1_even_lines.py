replaced_chars = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    for row, elements in enumerate(file):
        reversed_words = " ".join(elements.strip().split()[::-1])
        if row % 2 == 0:
            for ch in replaced_chars:
                reversed_words = reversed_words.replace(ch, "@")
            print(reversed_words)