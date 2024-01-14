from itertools import permutations

sets = [1,2,3]

data = itertools.permutation(sets, 2)

print(data)

for i in data:
   print(i)