def is_list_empty(lst):
    # Check if the list is empty
    return len(lst) == 0

# Input from the user
lst = list(map(int, input("Enter the list elements (space-separated): ").split()))

# Check if the list is empty
if is_list_empty(lst):
    print("The list is empty.")
else:
    print("The list is not empty.")
