

s = list(input())

print(len(s))

cnt = 0
tmp = s[0]
for i in range(1, len(s) - 1):  # 문자열의 길이만큼
    if (s[i] != tmp):
        cnt += 1
    tmp = s[i]


result = (cnt + 1) // 2

print(result)
