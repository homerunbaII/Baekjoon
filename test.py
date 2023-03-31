n = int(input())
r = 0

for i in range(1, n):
    print('i', i,)
    for j in range(i+1, n + 1):
        print('j', j, end=' ')
        for k in range(1, j+1):
            print(k, end='')
            r = r+1
        print()

print(r)
