def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

# Convert the iterator to a list to see the results
result = list(squared_numbers)
print(result)
