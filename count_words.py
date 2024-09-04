def count_words(s):
    # Split the string into words based on whitespace and count the length of the list
    words = s.split()
    return len(words)

# Input from the user
input_string = input("Enter a string: ")
word_count = count_words(input_string)

print(f"Number of words: {word_count}")
