# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.



text = input()
symbols = {}
for char in text:
    if char not in symbols:
        symbols[char] = 0
    symbols[char] += 1

# sorted returns a tuple with a key, value from the dict, sorted alphabetically by ASCII
for sym, count in sorted(symbols.items()):
    print(f'{sym}: {count} time/s')