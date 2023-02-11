m = int(input())
n = int(input())


def find_primenumber(num):
    if (num == 1):
        return 0
    for i in range(2, num):
        if (num % i == 0):
            return 0
    return num


primenumber_list = []
for i in range(m, n + 1):
    if (find_primenumber(i) > 0):
        primenumber_list.append(i)


if not primenumber_list:
    print(-1)
else:
    print(sum(primenumber_list))
    print(primenumber_list[0])
