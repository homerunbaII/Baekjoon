from collections import deque

n = int(input())

prefer = int(input())

order = list(map(int, input().split()))
# 후보 번호, 후보 추천수, 추천된 순서
q = []

for i in range(len(order)):
    # 후보가 q 내에 있는지 없는지 체크
    checker = [0,0]
    for j in range(len(q)):
        if q[j][0] == order[i]:
            # 인덱스 넘버
            checker = [1, j]
            break
    # 후보가 있다면
    if checker[0] == 1:
        q[checker[1]][1] += 1
    # 후보가 없다면
    else:
        # 아직 비어있다면
        if len(q) < n:
            q.append([order[i], 1, i])
        # 꽉찼다면
        else:
            del q[0]
            q.append([order[i], 1, i])  
    q.sort(key = lambda x : (x[1], x[2]))
        
q.sort(key = lambda x : x[0])

for i in q:
    print(i[0], end = ' ')