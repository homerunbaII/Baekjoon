x = int(input())  # 14

sum = 0
n = 1
while (n):
    sum += n  # 1, 3, 6, 10, 15까지
    if (sum >= x):
        break
    n += 1  # 2, 3, 4, 5번째

test = n + 1  # 분모와 분자의 합 = 6
location = x - (sum - n)  # 14-10=4, 5번째 줄에서 4번째 수


if (n % 2 == 0):  # n번째가 짝수라면
    print("{0}/{1}".format(location, test - location))
else:
    print("{0}/{1}".format(test - location, location))
