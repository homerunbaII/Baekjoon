def order1(array, i, x):
    array[i - 1] = x
    return array


def order2(array, l, r):
    for i in range(l-1, r):
        if (array[i] == 1):
            array[i] = 0
        else:
            array[i] = 1
    return array


def order3(array, l, r):
    for i in range(l-1, r):
        array[i] = 0
    return array


def order4(array, l, r):
    for i in range(l-1, r):
        array[i] = 1
    return array


n, m = map(int, input().split())
light_status = list(map(int, input().split()))

for i in range(m):
    ordernum, a, b = map(int, input().split())
    if (ordernum == 1):
        light_status = order1(light_status, a, b)
    if (ordernum == 2):
        light_status = order2(light_status, a, b)
    if (ordernum == 3):
        light_status = order3(light_status, a, b)
    if (ordernum == 4):
        light_status = order4(light_status, a, b)

print(*light_status)
