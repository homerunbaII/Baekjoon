t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = str(n % h)
    if (floor == '0'):
        floor = str(h)
        roomnum = str(n // h)
    else:
        roomnum = str(n // h + 1)
    roomnum = roomnum.zfill(2)
    print(floor+roomnum)
