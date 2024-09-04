def print_even_position_elements(arr):
    # Iterate over the array and print elements at even indices
    for index in range(0, len(arr), 2):  # Start at index 0 and step by 2
        print(arr[index])

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

print("Elements at even positions are:")
print_even_position_elements(arr)
