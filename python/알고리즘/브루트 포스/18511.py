from itertools import product

n, k = map(int, input().split())
len_max = len(str(n))
arr = list(input().split())


while True:
    tmp = list(product(arr, repeat=len_max))
    result = []
    for i in tmp:
        if int("".join(i)) <= n:
            result.append(int("".join(i)))

    if len(result) >= 1:
        print(max(result))
        break

    else:
        len_max -= 1
