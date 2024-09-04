def sum_of_elements(arr):
    # Use the sum() function to get the sum of all elements in the array
    return sum(arr)

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# Calculate the sum of elements
total_sum = sum_of_elements(arr)

print(f"The sum of all elements in the array is: {total_sum}")
