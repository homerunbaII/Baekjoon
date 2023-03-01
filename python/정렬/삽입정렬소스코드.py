array = [7, 9, 6, 5, 3, 1, 0, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자신보다 작은 데이터를 만나면 그 자리에 멈춘다
            break

print(array)
