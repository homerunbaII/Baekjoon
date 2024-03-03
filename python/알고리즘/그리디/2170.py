import sys 
input = sys.stdin.readline

n = int(input())

length = []

for i in range(n):
    x, y = map(int, input().split())
    length.append([x,y])

length.sort(key = lambda x: (x[0], x[1]))
left, right = length[0][0], length[0][1]
cnt = right - left

for i in range(1, len(length)):

    n_left, n_right = length[i][0], length[i][1]
    if n_left >= right:
        cnt += (n_right - n_left)
    elif n_left < n_right :
        if n_right <= right:
            pass
        else: 
            cnt += (n_right - right)
    # 다음 변수 선언
    if right >= n_right:
        pass
    else:
        right = n_right
        
    
print(cnt)
