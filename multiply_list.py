def multiply_items(lst):
    # Initialize the product to 1 (identity for multiplication)
    product = 1
    
    # Iterate through the list and multiply each item
    for item in lst:
        product *= item
    
    return product

# Input from the user
lst = list(map(int, input("Enter the list elements (space-separated): ").split()))

# Multiply all items in the list
result = multiply_items(lst)

print(f"The product of all items in the list is: {result}")
