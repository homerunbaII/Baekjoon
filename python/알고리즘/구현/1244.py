n = int(input())


def switch_invert(array, num):
    if array[num-1] == 1:
        array[num-1] = 0
    else:
        array[num-1] = 1


switch = list(map(int, input().split()))

p = int(input())

for i in range(p):
    s, num = map(int, input().split())
    if s == 1:
        k = num
        while (k <= n):
            switch_invert(switch, k)
            k += num
    if s == 2:
        j = 0
        switch_invert(switch, num)
        j += 1
        while (num - j >= 1 and num + j <= n):
            if switch[num + j-1] == switch[num - j-1]:
                switch_invert(switch, num + j)
                switch_invert(switch, num - j)
            else:
                break
            j += 1


for i in range(0, len(switch)):
    if (i+1) % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')
