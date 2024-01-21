import sys

input = sys.stdin.readline

n , less = map(int, input().split())
### [영단어, 개수] 가 들어갈 예정
word_list = {}

for i in range(n):
    word = input().rstrip()
    if len(word) < less:
        continue
    else:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

word_list = sorted(word_list.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in word_list:
    print(i[0])
