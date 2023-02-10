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

# N = int(input())
# cnt = 0 # 설탕 봉지 수
# while N >= 0:
#     if N % 5 == 0:
#         cnt += (N // 5)
#         print(cnt)
#         break
#     N -= 3
#     cnt += 1
# else:
#     print(-1)
