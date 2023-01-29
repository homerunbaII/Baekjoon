# 1. 알파벳을 입력받는다
# 2. 각 알파벳에 해당하는 시간을 리스트, 혹은 딕셔너리를 이용하여 형성
# 3. 알파벳을 순환화여 각 알파벳에 해당하는 초를 sum에 +=을 이용하여 계산

# alphabet = list(input())
# time = {'A': 3, 'B': 3, 'C': 3, 'D': 4, 'E': 4, 'F': 4, 'G': 5, 'H': 5, 'I': 5, 'J': 6, 'K': 6, 'L': 6, 'M': 7,
#         'N': 7, 'O': 7, 'P': 8, 'Q': 8, 'R': 8, 'S': 8, 'T': 9, 'U': 9, 'V': 9, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}

# sum = 0
# for i in alphabet:
#     sum += time[i]

# print(sum)


# 좋은 코드로 수정

alphabet = list(input())  # DEA

time = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

sum = 0

for i in time:  # 'ABC'
    for j in alphabet:  # 'D', 'E', 'A'
        if j in i:
            sum += time.index(i)+3

print(sum)
