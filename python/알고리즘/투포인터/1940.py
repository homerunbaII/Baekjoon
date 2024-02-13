n = int(input())
m = int(input())

ingredient = {}
cnt = 0
num = list(map(int, input().split()))

for i in num:
    ingredient[i] = 1

for i in num:
    if (m - i) in ingredient:
        cnt += 1

print(cnt//2)