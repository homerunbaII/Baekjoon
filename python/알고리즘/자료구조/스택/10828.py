import sys


def push(array, x):
    return array.append(x)


def pop(array):
    if not array:
        print(-1)
    else:
        print(array.pop())
    return


def size(array):
    print(len(array))


def empty(array):
    if not array:
        print(1)
    else:
        print(0)


def top(array):
    if not array:
        print(-1)
    else:
        print(array[-1])


n = int(input())

array = []

for i in range(n):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        order, x = order.split()
        push(array, x)
    if order == 'pop':
        pop(array)
    if order == 'size':
        size(array)
    if order == 'empty':
        empty(array)
    if order == 'top':
        top(array)
