import sys

input = sys.stdin.readline

n = int(input())

vec = []

for i in range(n):
    x,y = map(int, input().split())
    vec.append([x,y])

vec.sort(key = lambda x : (x[0], x[1]))

for i in vec:
    print(i[0], i[1])