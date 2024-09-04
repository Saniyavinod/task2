def count_case_letters(s):
    # Initialize counters for uppercase and lowercase letters
    upper_count = 0
    lower_count = 0
    
    # Iterate through each character in the string
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

# Input from the user
input_string = input("Enter a string: ")

# Count uppercase and lowercase letters
upper_count, lower_count = count_case_letters(input_string)

print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")
