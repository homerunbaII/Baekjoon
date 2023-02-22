n = list(map(int, str(input())))

total = sum(n)

if (total % 3 != 0):
    print(-1)
elif 0 not in n:
    print(-1)
else:
    n.sort(reverse=True)
    for i in n:
        print(i, end='')
