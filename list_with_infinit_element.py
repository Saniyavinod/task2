def infinite_generator(start=0):
    while True:
        yield start
        start += 1

# Create an infinite generator
gen = infinite_generator()

# Print the first 10 elements from the infinite generator
print("First 10 elements from the infinite generator:")
for _ in range(10):
    print(next(gen))
