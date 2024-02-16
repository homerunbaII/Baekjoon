x, y, w, s = map(int, input().split())

time = 0

# 대각선의 가중치가 낮다면 대각선 이동
if 2 * w >= s:
    sum = min(x,y)
    time += s * sum
    x -= sum
    y -= sum

# 홀수 제거 -> 다음 대각선 가중치 비교 때 대각선 이동을 가능하게 하기 위해서
if y % 2 != 0:
    y -= 1
    time += w
if x % 2 != 0:
    x -= 1
    time += w
 
# 대각선 혹은 평행 이동s
if w > s:
    time += y * s + x * s
else:
    time += y * w + x * w



print(time)
        
