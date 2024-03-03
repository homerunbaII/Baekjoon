n, s = map(int, input().split())
n_list = list(map(int, input().split()))

small = 10e9

p1, p2 = 0,0
total = 0

while True:
    if total >= s :
        small = min(p2 - p1, small)
        total -= n_list[p1]
        p1 += 1
    elif p2 == n:
        break
    else:
        total += n_list[p2]
        p2 += 1

if small == 10e9:
    print(0)
else:
    print(small)
        


    