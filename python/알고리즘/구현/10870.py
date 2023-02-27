n = int(input())
result = 0
n_2 = 0
n_1 = 1

if n == 0:
    print(0)
else:
    for _ in range(n-1):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    print(result)
