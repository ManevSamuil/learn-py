set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 1} 

# union of sets
union_set = set1 | set2
print(union_set)  

# difference of set
difference_set = set1.difference(set2)
print(difference_set)

# is sub set
issub_set = set1.issubset(set2)
print(issub_set)

# intersection
intersection_set = set1 & set2
print(intersection_set)