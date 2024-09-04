def is_harshad_number(num):
    if num <= 0:
        return False  # Harshad numbers are positive integers
    
    # Convert the number to a string to iterate over each digit
    digits = str(num)
    
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in digits)
    
    # Check if the number is divisible by the sum of its digits
    return num % sum_of_digits == 0

# Example usage
number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number.")
else:
    print(f"{number} is not a Harshad number.")
