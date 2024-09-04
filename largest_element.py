def find_largest_element(arr):
    # Use the max() function to find the largest element in the array
    return max(arr)

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# Ensure the array is not empty
if arr:
    largest_element = find_largest_element(arr)
    print(f"The largest element in the array is: {largest_element}")
else:
    print("The array is empty.")

