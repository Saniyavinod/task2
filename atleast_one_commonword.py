def have_common_element(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)
    
    # Check if there is any intersection between the two sets
    return not set1.isdisjoint(set2)

# Input from the user
list1 = input("Enter the first list of elements (comma-separated): ").split(',')
list2 = input("Enter the second list of elements (comma-separated): ").split(',')

# Remove leading/trailing whitespace from each element
list1 = [element.strip() for element in list1]
list2 = [element.strip() for element in list2]

if have_common_element(list1, list2):
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common elements.")
