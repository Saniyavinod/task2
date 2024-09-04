def reverse_string(s):
    # Reverse the string using slicing
    return s[::-1]

# Input from the user
input_string = input("Enter a string: ")

# Get the reversed string
reversed_string = reverse_string(input_string)

print(f"The reversed string is: {reversed_string}")
