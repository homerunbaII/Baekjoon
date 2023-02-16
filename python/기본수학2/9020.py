import sys

input = sys.stdin.readline


def find_primenumber(num):  # 소수 찾는 메서드
    if (num == 1):
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            return 0
    return num


def find_nearnum(num, list):  # 리스트 내 가장 근사한 값을 찾는 메서드
    while (True):
        for i in list:
            if (i == num):
                return num
        num -= 1


primenumber_list = []

for i in range(1, 10001):  # 1 ~~ 10000까지 소수 리스트 구하기
    if (find_primenumber(i) > 0):
        primenumber_list.append(i)

t = int(input())

for i in range(t):
    num = int(input())  # num 입력받기
    p1 = int(num / 2)  # num 2로 나누기
    # 2로 나눈 값 primenumber_list에서 근사소수값 찾기
    middle_primenum_1 = find_nearnum(p1, primenumber_list)
    location = primenumber_list.index(middle_primenum_1)  # 근사소수값의 인덱스 위치 반환
    while (True):
        middle_primenum_2 = num - middle_primenum_1  # 소수
        if find_primenumber(middle_primenum_2) > 0:
            print(middle_primenum_1, middle_primenum_2)
            break
        else:
            location -= 1  # 인덱스 값 1 감소
            middle_primenum_1 = primenumber_list[location]  # 세로운 중앙 소수값 대입
