n = input()

duck = 0
duck_max = 0
flag = 0

q = 0
u = 0
a = 0
c = 0
k = 0

for i in n:
    if i == 'q':
        q += 1
    if i == 'u':
        u += 1
    if i == 'a':
        a += 1
    if i == 'c':
        c += 1
    if i == 'k':
        k += 1
    if q < u or u < a or a < c or c < k:
        flag = -1
        break

if q == u == a == c == k:
    pass
else:
    flag = -1

for i in n:
    if i == 'q':
        duck += 1
    if i == 'k':
        duck -= 1
    if duck > duck_max:
        duck_max = duck

if flag == -1:
    print(-1)
else:
    print(duck_max)
