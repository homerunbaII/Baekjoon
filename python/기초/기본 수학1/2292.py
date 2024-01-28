"""
규칙 파악
1번째 방 1
2번쨰 방 1 + 6
3번째 방 1 + 6 + 12 
4번쨰 방 1 + 6 + 12 + 18"""

n = int(input())  # 19
sum = 1
i = 1

while (i):
    if (n == 1):
        i = 1
        break
    if (sum >= n):
        break
    sum += 6 * i  # 7, 19
    i += 1

print(i)
