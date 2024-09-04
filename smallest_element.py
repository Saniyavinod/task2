def find_smallest_element(arr):
    # Use the min() function to find the smallest element in the array
    return min(arr)

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# Ensure the array is not empty
if arr:
    smallest_element = find_smallest_element(arr)
    print(f"The smallest element in the array is: {smallest_element}")
else:
    print("The array is empty.")
