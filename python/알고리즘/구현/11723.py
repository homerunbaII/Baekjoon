import sys

n = int(input())
s = []

for i in range(n):
    line = sys.stdin.readline().rstrip()
    line = line.split()
    if len(line) == 1:
        func = line[0]
    else:
        func = line[0] 
        x = line[1]
        x = int(x)
    if func == 'add':
        if x in s:
            pass
        else:
            s.append(x) 
    if func == 'remove':
        if x in s:
            s.remove(x)
        else:
            pass
    if func == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    if func == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    if func == 'all':
        s = [i for i in range(1, 21)]
    if func == 'empty':
        s = []
