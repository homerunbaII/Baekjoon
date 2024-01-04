n = int(input())
height_list = list(map(int, input().split()))
order_list = [0] * 10


# i 는 1부터이다
for i in range(1, n + 1):
    checker = 0
    for j in range(n):
        if order_list[j] != 0:
            continue
        if checker == height_list[i - 1]:
            if order_list[j] == 0:
                order_list[j] = i
                break
            else: continue
        if i > order_list[j] :
            checker += 1

for i in range(n):
    print(order_list[i], end = ' ')