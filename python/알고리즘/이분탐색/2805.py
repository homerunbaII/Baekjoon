from numpy import mean
import math

n , target = map(int,input().split())
tree = list(map(int,input().split()))

start, end = 1, sum(tree)

while start  <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in tree :
        if i > mid:
            cnt += i - mid 
    if cnt >= target:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)
