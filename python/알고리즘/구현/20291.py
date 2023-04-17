import sys

input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n):
    a, b = input().rstrip().split('.')
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1

s_dic = sorted(dic.items())

for i in s_dic:
    print(i[0], i[1])
