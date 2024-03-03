n = int(input())

length = []

for i in range(n):
    x, y = map(int, input().split())
    length.append([x,y])

length.sort()
left, right = length[0][0], length[0][1]

cnt = length[0][1] - length[0][0]

for i in range(1, len(length)):
    n_left, n_right = length[i][0], length[i][1]
    # 다음 x가 이전 y보다 클 때  1 3, 5 6
    if n_left >= right:
        cnt += (n_right - n_left)
    elif n_left < n_right :
        if n_right <= right:
            continue
        else: 
            cnt += (n_right - right)
    
print(cnt)
