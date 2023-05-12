import sys

input = sys.stdin.readline

n = int(input())

money = []

result = 0

for i in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for i in range(len(money)):
    if money[i] - i < 0:
        break
    result += money[i] - i

print(result)
