def find_primenumber(num):  # 소수를 판별하는 메서드
    if (num == 1):
        return 0
    for i in range(2, num):
        if (num % i == 0):
            return 0
    return num


def find_primenumber2(num, list):  # 아르토스테네스의 체
    if (num == 1):
        return 0
    for i in list:
        if (num % i == 0):
            if (num == i):
                return num
            else:
                return 0
    return num


primenum_list = []  # 루트n까지의 소수 리스트

for i in range(1, int(246912 ** (1/2)) + 1):
    if (find_primenumber(i) > 0):
        primenum_list.append(i)

fianl_primenum_list = []
for i in range(1, 246912):  # 아리토스테네스의 체
    if (find_primenumber2(i, primenum_list) > 0):
        fianl_primenum_list.append(i)  # 체로 걸러진 1~ 246912까지의 소수

n = int(input())

while (n):
    cnt = 0
    for i in fianl_primenum_list:
        if n < i <= 2*n:  # 범위 내에 있으면 카운트 + 1
            cnt += 1

    print(cnt)
    n = int(input())
