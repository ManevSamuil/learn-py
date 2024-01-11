# filter() is used to filter a list from a list

# for even numbers
def is_even(x):
    return x % 2 == 0


# for odd numbers
def is_odd(x):
    return x % 2 == 0


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = list(filter(is_odd, my_list))
even_numbers = list(filter(is_even, my_list))

print(f"my_odd_numbers {odd_numbers}")
print(f"my_even_numbers {even_numbers}")
print(f"from {my_list} -> {odd_numbers}")
