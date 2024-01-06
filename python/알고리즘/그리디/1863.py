import sys

input = sys.stdin.readline

n = int(input())



height = []
building = 0

for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        height = []
        continue
    elif len(height) != 0 and height[-1] > y:
        temp = []
        for j in height:
            if j > y:
                temp.append(j)
        for k in temp:
            height.remove(k)
    if y not in height:
        height.append(y)
        building += 1
    else:
        continue

print(building)
    
    