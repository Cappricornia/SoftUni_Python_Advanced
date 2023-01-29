'''Write a recursive function called palindrome() that will receive a word and an index (always 0).
Implement the function, so it returns "{word} is a palindrome"
if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion.
Submit only the function in the judge system.'''


def palindrome(word, ind):
    # base case
    if ind == len(word) // 2:
        return f"{word} is a palindrome"

    left_element = word[ind]
    right_element = word[len(word) - 1 - ind]

    if left_element != right_element:
        return f"{word} is not a palindrome"

    return palindrome(word, ind + 1)


print(palindrome("abcba", 0))  # index always 0