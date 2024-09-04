def find_max_of_three(a, b, c):
    # Compare the numbers to find the maximum
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

maximum = find_max_of_three(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}")
