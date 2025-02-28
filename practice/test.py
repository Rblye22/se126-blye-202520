# Initialize the dictionary
dictionary = {}

# Function to add a word and its definition
def add_word(dictionary, word, definition):
    dictionary[word] = definition
    return dictionary

# Example usage
word = "Empathy"
definition = "The ability to understand and share the feelings of another."

# Adding the word and definition to the dictionary
updated_dictionary = add_word(dictionary, word, definition)

# Print the updated dictionary
print(updated_dictionary)