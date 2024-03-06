import math

n, l = map(int, input().split())
location = list(map(int, input().split()))

location.sort()

cnt = 0
tape = location[0]
for i in location:
    if tape <= i:
        cnt += 1
        tape = (i + l)

print(cnt)
    
