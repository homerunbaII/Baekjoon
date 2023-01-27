word = input().upper()  # apple -> APPLE
word_list = list(set(word))  # [A, P, L ,E]

cnt = []

for i in word_list:  # [A, P, L, E]
    cnt.append(word.count(i))  # [1,2,1,1]

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    # max(cnt) 즉 최대 개수의 위치 = cnt의 1번째 index, -> 이 인덱스는 word_list의 순서와 일치한다
    print(word_list[cnt.index(max(cnt))])
