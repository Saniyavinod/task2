def remove_even_numbers(lst):
    # Create a new list with only the odd numbers
    return [num for num in lst if num % 2 != 0]

# Input from the user
lst = list(map(int, input("Enter the list elements (space-separated): ").split()))

# Remove even numbers from the list
result = remove_even_numbers(lst)

print("List after removing even numbers:", result)
