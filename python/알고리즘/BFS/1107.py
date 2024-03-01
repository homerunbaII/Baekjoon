target = int(input())
ans = abs(100 - target) 
m = int(input())
if m: 
    broken = list(input().split())
else:
    broken = []

for num in range(1000001): 
    for N in str(num):
        if N in broken: 
            break
    else: 
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)