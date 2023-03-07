from collections import deque

t = int(input())

for i in range(t):
    n, target = map(int, input().split())     # 문서의 총 개수, 찾을 문서의 인덱스 위치
    que = deque(list(map(int, input().split())))  # 중요도제시
    cnt = 1
    while (que):
        if que[0] == max(que):  # 만약 popleft할 대상이 가장 큰 숫자라면
            if target == 0:  # 만약 타겟인덱스였다면
                print(cnt)
                break
            else:
                que.popleft()  # 타겟이 아니었다면 popleft()
                cnt += 1  # 카운트 ++
                target -= 1  # 타겟 넘버는 인덱스 위치 1 감소
        else:  # 더 큰 숫자가 있다면
            que.append(que.popleft())
            if target == 0:  # 타겟이 인덱스가 0이었다면
                target = len(que) - 1  # popleft()후 append 했으니 인덱스 넘버 끝으로 초기화
            else:
                target -= 1  # 타켓 인덱스 감소
