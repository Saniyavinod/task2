def count_elements(arr):
    # Use the len() function to count the number of elements in the array
    return len(arr)

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# Get the number of elements
number_of_elements = count_elements(arr)

print(f"The number of elements in the array is: {number_of_elements}")
