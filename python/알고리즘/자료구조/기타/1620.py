n, m = map(int, input().split())

pockemon = {}

for i in range(1, n+1):
    x = input()
    pockemon.setdefault('%d' % (i), x)

pockemon_reverse = {v: k for k, v in pockemon.items()}

print(pockemon_reverse)
for i in range(m):
    k = input()
    if k.isdigit() == True:
        print(pockemon['%d' % (int(k))])
    else:
        print(pockemon_reverse[k])
