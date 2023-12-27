a, b, c = map(int, input().split())
cost_list = []
cost = 0

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        cost_list.append(j)

for i in range(1, 101):
    cost_stack = 0
    for j in cost_list:
        if j == i:
            cost_stack += 1
    if cost_stack == 1:
        cost += a
    elif cost_stack == 2:
        cost += b * 2
    elif cost_stack == 3:
        cost += c * 3

print(cost)
