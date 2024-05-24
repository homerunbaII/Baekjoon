import sys, math
input = sys.stdin.readline

n = int(input())
arr = []
dic = {}

for i in range(n):
    k = int(input())
    arr.append(k)
    if k in dic:
        dic[k] += 1
    else :
        dic[k] = 1

arr.sort()
temp = []

for key, value in dic.items():
    temp.append([key, value])

temp.sort(key = lambda x : (-x[1], x[0]))

if len(temp) == 1:
    frequent = temp[0][0]
else:
    if temp[0][1] > temp[1][1]:
        frequent = temp[0][0]
    else:
        frequent = temp[1][0]

avg = int(round((sum(arr) / n)))
middle = arr[(n // 2)]
mini = arr[0] 
maxi = arr[n -1]

print(avg)
print(middle)
print(frequent)
print(maxi - mini)