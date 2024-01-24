s = list(input())
cnt_0 = 0
cnt_1 = 1
for i in s:
    if i == '0':
        cnt_0 += 1
    if i == '1':
        cnt_1 += 1

cnt_0 = cnt_0 // 2
cnt_1 = cnt_1 // 2

delete_cnt = 0
i = 0

while cnt_1 > 0:
    if s[i] == '1':
        del s[i]
        cnt_1 -= 1
        i -= 1
    i += 1

while cnt_1 > 0:
    if s[i] == '1':
        del s[i]
        cnt_1 -= 1
        i -= 1
    i += 1

i = len(s) - 1
while cnt_0 > 0:
    if s[i] == '0':
        del s[i]
        print(s)
        cnt_0 -= 1
        i -= 1
    i -= 1
    print(s[i])

print(''.join(s))


    


