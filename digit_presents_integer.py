def count_digits(number):
    # Convert the number to a string and exclude the negative sign if present
    return len(str(abs(number)))

# Input from the user
number = int(input("Enter an integer: "))

# Count the number of digits
digit_count = count_digits(number)

print(f"The number of digits in {number} is: {digit_count}")
