import sys

n, m = map(int, input().split())

pockemon = {}

for i in range(1, n+1):
    x = sys.stdin.readline().rstrip()
    pockemon.setdefault('%d' % (i), x)

pockemon_reverse = {v: k for k, v in pockemon.items()}

for i in range(m):
    k = sys.stdin.readline().rstrip()
    if k.isdigit() == True:
        print(pockemon['%d' % (int(k))])
    else:
        print(pockemon_reverse[k])
