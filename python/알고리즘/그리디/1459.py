x, y, w, s = map(int, input().split())

time = 0

if 2 * w >= s:
    sum = min(x,y)
    time += s * sum
    x -= sum
    y -= sum

print(x,y)

if y % 2 != 0:
    y -= 1
    time += w
if x % 2 != 0:
    x -= 1
    time += w

print(x,y)    

if w > s:
    time += y * s + x * s
    x = 0
    y = 0
else:
    time += y * w + x * w
    x = 0
    y  = 0

print(x,y)


print(time)
        
