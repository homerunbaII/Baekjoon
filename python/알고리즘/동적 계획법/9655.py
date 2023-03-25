n = int(input())

rock = [0 for _ in range(1001)]

rock[1] = 1  # 상근
rock[2] = 0  # 창영
rock[3] = 1  # 상근

for i in range(4, n+1):
    if rock[i - 1] == 1 or rock[i - 3] == 1:
        rock[i] = 0
    else:  # rock[i - 1] ==  or rock[i - 3] == 1
        rock[i] = 1

if rock[n] == 1:
    print("SK")
else:
    print("CY")
