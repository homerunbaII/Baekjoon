a = [1, 2, 3]
n = 3


def func(i):
    if i == n:
        print(a)
    else:
        func(i + 1)
        for j in range(i+1, n+1):
            a[i-1], a[j-1] = a[j-1], a[i-1]
            func(i+1)
            a[i-1], a[j-1] = a[j-1], a[i-1]


func(1)
