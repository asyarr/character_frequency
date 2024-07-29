def sort_by_character_frequency(words, character):
    # Sorts an array of words based on the frequency of a specific character.
    # Function to calculate the frequency of a character in a word
    def character_frequency(word):
        return word.count(character)

    # Sort the words based on the frequency of the character
    sorted_words = sorted(words, key=character_frequency, reverse=True)
    return sorted_words

# List of words:
words = ["Learning", "AI", "Gamma", "CollegeEntranceExam", "Mathematics", "Portuguese"]
character = "a"

# Call the function to sort the words
sorted_words = sort_by_character_frequency(words, character)
# Return the sorted list
print(sorted_words)
