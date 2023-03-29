n = int(input())
r = 0

for i in range(1, n):
    for j in range(i+1, n):
        for k in range(1, j+1):
            r = r+1

print(r)
