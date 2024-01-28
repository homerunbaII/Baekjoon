s = list(input())
cnt_0, cnt_1 = s.count('0') // 2, s.count('1') // 2

for _ in range(cnt_1):
    s.pop(s.index('1'))
print(s)
for _ in range(cnt_0):
    s.pop(-s[::1].index('0')-1)
    print(s)

print(''.join(s))


    