from collections import deque

t = int(input())


for _ in range(t):
    cnt = 0 
    error_flag = False
    p = input()
    n = int(input())
    deq = deque(input().split(','))
    # 문자열 슬라이싱
    if n == 1:
        deq[0] = deq[0][1:-1]
    elif n == 0:
        deq = []
    else:
        deq[0] = deq[0][1:]
        deq[-1] = deq[-1][:-1]
    # 연산 수행
    for i in p :
        if i == 'R':
            cnt += 1
        else:
            if len(deq) == 0:
                print('error')
                error_flag = 1
                break
            else:
                if cnt % 2 == 0:
                    deq.popleft()
                    pass
                else:
                    deq.pop()
    #출력
    if error_flag == 1:
        continue
    if len(deq) == 0:
        print(deq)
    elif cnt % 2  == 0:
        print(f"[{','.join(deq)}]")
    else:
        deq.reverse()
        print(f"[{','.join(deq)}]")


