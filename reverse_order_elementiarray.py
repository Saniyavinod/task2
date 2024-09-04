def reverse_list(lst):
    # Reverse the list in place
    lst.reverse()
    return lst

# Input from the user
lst = list(map(int, input("Enter the list elements (space-separated): ").split()))

# Reverse the list
reversed_list = reverse_list(lst)

print("Reversed list:", reversed_list)
