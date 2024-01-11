my_list = ('apple', 'banana', 'mango')

for i, word in enumerate(my_list):
    for j, letter in enumerate(word):

        print(f"Index: {i}, {j}, Value: {letter}")
    print()

