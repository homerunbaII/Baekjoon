from itertools import combinations, permutations

n , m = map(int, input().split())
arr = [-1, 0 , 1]
result = permutations(arr, 3)
print(list(result))

# for i in range(n):

