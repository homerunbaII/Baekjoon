m, n = map(int, input().split())  # 10 40

prime_end = int(n ** (1/2))  # 소수 검사할 때, n의 루트까지만 순회하면 된다 # 6


def find_primenumber(num):
    if (num == 1):
        return 0
    for i in range(2, num):
        if (num % i == 0):
            return 0
    return num


primenum_list = []

for i in range(1, prime_end + 1):  # 1 ~ 6
    if (find_primenumber(i) > 0):
        primenum_list.append(i)


for j in range(m, n + 1):  # 10 40
    if (j == 1):
        continue
    cnt = len(primenum_list)
    for i in primenum_list:  # [2, 3 ,5]
        if (j % i == 0):
            if (j == i):
                print(j)
            else:
                break
        else:
            cnt -= 1
    if (cnt == 0):
        print(j)
