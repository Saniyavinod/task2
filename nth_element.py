def check_nth_element_exists(lst, n):
    # Check if the index n-1 is within the bounds of the list
    return 0 <= (n - 1) < len(lst)

# Input from the user
lst = list(map(int, input("Enter the list elements (space-separated): ").split()))
n = int(input("Enter the position to check (1-based index): "))

# Check if the n-th element exists
if check_nth_element_exists(lst, n):
    print(f"The {n}-th element exists in the list.")
else:
    print(f"The {n}-th element does not exist in the list.")
