def checkBingo(array):
    bingo_cnt = 0
    for i in range(5):
        if (array[i][0] == array[i][1] == array[i][2] == array[i][3] == array[i][4] == 'None'):
            bingo_cnt += 1
    for j in range(5):
        if (array[0][j] == array[1][j] == array[2][j] == array[3][j] == array[4][j] == 'None'):
            bingo_cnt += 1
    if array[0][0] == array[1][1] == array[2][2] == array[3][3] == array[4][4] == 'None':
        bingo_cnt += 1
    if array[0][4] == array[1][3] == array[2][2] == array[3][1] == array[4][0] == 'None':
        bingo_cnt += 1
    return bingo_cnt


bingo_list = []
num_list = []
num_cnt = 0
breaker = False

for _ in range(5):
    bingo_list.append(list(input().split()))
for _ in range(5):
    num_list.append(list(input().split()))


for i in range(5):
    for j in range(5):
        bingo_num = num_list[i][j]  # 사회자가 부르는 넘버
        num_cnt += 1  # 몇번재 num 인지
        for k in range(5):  # 부른 숫자를 None으로 대체
            for l in range(5):
                if bingo_list[k][l] == bingo_num:  # 리스트의 원소가 사회자가 부른 넘버와 같다면
                    bingo_list[k][l] = 'None'
        if (checkBingo(bingo_list) >= 3):  # 빙고가 3개이상이 되면
            breaker = True
            print(num_cnt)
            break
    if (breaker == True):  # 이중 for문 탈출
        break


print(bingo_list)
