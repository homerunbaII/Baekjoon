import sys

input = sys.stdin.readline

n , less = map(int, input().split()) ### 7 4 스페이스바   [들어올 단어 수 7, 최소 단어 길이 4 -> 4보다 작은 단어는 안외울거야]
### [영단어, 개수] 가 들어갈 예정 [[apple, 2], [sand ,1]]
word_list = {} # 검색속도 매우 빠름, BUT 메모리 할당 많이 해야함

for i in range(n): # 7 번 반복
    word = input().rstrip() 
    if len(word) < less:
        continue
    else:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1


word_list = sorted(word_list.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
print(word_list)
for i in word_list:
    print(i[0])
