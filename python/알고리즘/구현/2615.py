import sys

input = sys.stdin.readline

mok = []
flag = 0
breaker1 = False
breaker2 = False

for _ in range(19):
    mok.append(list(map(int, input().split())))


for k in range(1, 3):
    if breaker1 == True:
        break
    for i in range(19):
        if breaker1 == True:
            break
        for j in range(19):
            try:
                if k == mok[i][j] and mok[i][j] == mok[i][j + 1] and mok[i][j + 1] == mok[i][j + 2] and mok[i][j + 2] == mok[i][j + 3] and mok[i][j + 3] == mok[i][j + 4]:
                    flag = k
                try:
                    if flag == k and mok[i][j] == mok[i][j-1]:
                        flag = 0
                except IndexError:
                    pass
                try:
                    if flag == k and mok[i][j+4] == mok[i][j+5]:
                        flag = 0
                except IndexError:
                    pass
            except IndexError:
                pass
            if flag == k:
                column = i + 1
                row = j + 1
                breaker1 = True
                break
            try:
                if k == mok[i][j] and mok[i][j] == mok[i+1][j + 1] and mok[i+1][j + 1] == mok[i+2][j + 2] and mok[i+2][j + 2] == mok[i+3][j + 3] and mok[i+3][j + 3] == mok[i+4][j + 4]:
                    flag = k
                try:
                    if flag == k and mok[i][j] == mok[i-1][j-1]:
                        flag = 0
                except IndexError:
                    pass
                try:
                    if flag == k and mok[i+4][j+4] == mok[i+5][j+5]:
                        flag = 0
                except IndexError:
                    pass
            except IndexError:
                pass
            if flag == k:
                column = i + 1
                row = j + 1
                breaker1 = True
                break
            try:
                if k == mok[i][j] and mok[i][j] == mok[i + 1][j] and mok[i + 1][j] == mok[i + 2][j] and mok[i + 2][j] == mok[i + 3][j] and mok[i + 3][j] == mok[i + 4][j]:
                    flag = k
                try:
                    if flag == k and mok[i][j] == mok[i-1][j]:
                        flag = 0
                except IndexError:
                    pass
                try:
                    if flag == k and mok[i+4][j] == mok[i+5][j]:
                        flag = 0
                except IndexError:
                    pass
            except IndexError:
                pass
            if flag == k:
                column = i + 1
                row = j + 1
                breaker1 = True
                break
            try:
                if k == mok[i][j] and mok[i][j] == mok[i - 1][j + 1] and mok[i - 1][j + 1] == mok[i - 2][j+2] and mok[i - 2][j+2] == mok[i - 3][j+3] and mok[i - 3][j+3] == mok[i - 4][j+4]:
                    flag = k
                try:
                    if flag == k and mok[i][j] == mok[i+1][j-1]:
                        flag = 0
                except IndexError:
                    pass
                try:
                    if flag == k and mok[i-4][j + 4] == mok[i-5][j+5]:
                        flag = 0
                except IndexError:
                    pass
            except IndexError:
                pass
            if flag == k:
                column = i + 1
                row = j + 1
                breaker1 = True
                break

if flag == 1 or flag == 2:
    print(flag)
    print(column, row)
else:
    print(0)
