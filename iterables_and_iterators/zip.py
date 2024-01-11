list1 = (1, 2, 3)
list2 = ('a', 'b', 'c')

zipped = list(zip(list1, list2))

# print(zipped)
for i, val in enumerate(zip(list1, list2)):
   print(f"val {val} at {i}")