import sys

input = sys.stdin.readline

n, m = map(int, input().split())

train_list = []
order_list = []
pass_list = []

for _ in range(n):
    train_list.append([0 for _ in range(20)])

for _ in range(m):
    order_list.append(list(map(int, input().split())))


def t1(n, m):
    train_list[n-1][m-1] = 1


def t2(n, m):
    train_list[n-1][m-1] = 0


def t3(n):
    train_list[n-1].insert(0, 0)
    train_list[n-1].pop()


def t4(n):
    train_list[n-1].append(0)
    del train_list[n-1][0]


for i in range(m):
    if order_list[i][0] == 1:
        t1(order_list[i][1], order_list[i][2])
    if order_list[i][0] == 2:
        t2(order_list[i][1], order_list[i][2])
    if order_list[i][0] == 3:
        t3(order_list[i][1])
    if order_list[i][0] == 4:
        t4(order_list[i][1])

for j in train_list:
    if j not in pass_list:
        pass_list.append(j)


print(len(pass_list))
