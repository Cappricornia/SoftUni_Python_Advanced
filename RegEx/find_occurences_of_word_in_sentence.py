# Find occurrence of word in a sentence


import re
sentence = input()
searched_word = input()
matches = re.findall(fr"\b{searched_word}\b", sentence, re.IGNORECASE)
print(len(matches))


