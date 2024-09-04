def find_duplicates(arr):
    # Dictionary to store the frequency of each element
    element_count = {}
    
    # Populate the dictionary with element counts
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    # Print the elements that have more than one occurrence
    duplicates = [element for element, count in element_count.items() if count > 1]
    
    return duplicates

# Input from the user
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

duplicates = find_duplicates(arr)

if duplicates:
    print("Duplicate elements are:", duplicates)
else:
    print("No duplicate elements found.")
