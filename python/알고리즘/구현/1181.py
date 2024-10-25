import sys

input = sys.stdin.readline

n = int(input())

word = []

for i in range(n):
    new = input().rstrip()
    word.append(new)

word = list(set(word))

word.sort(key = lambda x : (len(x), x))

print("\n".join(word))