# def print_upper_words(words):
#     """Print words passed in array"""

#     upper_case_words = (word.upper() for word in words)
#     next_word = next(upper_case_words, None)
#     while next_word is not None:
#         if next_word[0] == "e" or next_word[0] == "E":
#             print(next_word)
#             break
#         else:
#             next_word = next(upper_case_words, None)


# print(print_upper_words.__doc__)
# print_upper_words(["Jerraill", "Sarah", "Nariayh", "Eli", "Sierrah", "Lelah"])


def print_upper_words(words, starting_letters):
    """only prints words that start with startingLetters"""

    for word in words:
        if word[0] in starting_letters or word[0].upper() in starting_letters:
            print(word)


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})
