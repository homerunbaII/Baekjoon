import sys

input = sys.stdin.readline

n = int(input())

member = []

for i in range(n):
    age, name = input().rstrip().split()
    age = int(age)
    member.append([age, i , name])

member.sort(key = lambda x : (x[0], x[1]))

for i in range(n):
    print(member[i][0], member[i][2])