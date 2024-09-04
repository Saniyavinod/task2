def copy_list_slicing(lst):
    # Copy the list using slicing
    return lst[:]

def copy_list_copy_method(lst):
    # Copy the list using the copy() method
    return lst.copy()

def copy_list_constructor(lst):
    # Copy the list using the list() constructor
    return list(lst)

# Input from the user
original_list = list(map(int, input("Enter the list elements (space-separated): ").split()))

# Clone the list using different methods
cloned_list_slicing = copy_list_slicing(original_list)
cloned_list_copy_method = copy_list_copy_method(original_list)
cloned_list_constructor = copy_list_constructor(original_list)

print("Original list:", original_list)
print("Cloned list (slicing):", cloned_list_slicing)
print("Cloned list (copy method):", cloned_list_copy_method)
print("Cloned list (list constructor):", cloned_list_constructor)
