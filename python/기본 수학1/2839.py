n = int(input())
i = 0
while (n):  # 29
    a = n // 5 - i  # 5 - 0, 5 - 1
    if (a == -1):
        print(a)
        break
    if ((n - a * 5) % 3 == 0):  # 4 % 3, 9 % 3
        print(int(a + (n - a * 5) / 3))
        break
    i += 1
