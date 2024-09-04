def print_odd_position_elements(arr):
    # Iterate over the array and print elements at odd indices
    for index in range(1, len(arr), 2):  # Start at index 1 and step by 2
        print(arr[index])

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

print("Elements at odd positions are:")
print_odd_position_elements(arr)
