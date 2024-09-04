import random

def shuffle_list(lst):
    # Shuffle the list in place
    random.shuffle(lst)
    return lst

# Input from the user
lst = list(map(int, input("Enter the list elements (space-separated): ").split()))

# Shuffle the list
shuffled_list = shuffle_list(lst)

print("Shuffled list:", shuffled_list)
