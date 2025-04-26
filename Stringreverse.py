def reverse_string(word):
    new_word = ""  # Start with an empty string
    for letter in word:  # Go through each letter
        new_word = letter + new_word  # Put the letter in front
    return new_word
# trial
print(reverse_string("hello"))  # Should print "olleh"
