import sys

input = sys.stdin.readline

n , m = map(int, input().split())


d_dict = {}
b_dict = {}
dbj = []

for i in range(n):
    name = input().rstrip()
    d_dict[name] = 1

for i in range(m):
    name = input().rstrip()
    b_dict[name] = 1

for i in d_dict:
    if i in b_dict:
        dbj.append(i)

dbj.sort()

print(len(dbj))
for i in dbj:
    print(i)