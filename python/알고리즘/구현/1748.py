# n 이라는 수까지 자리수가 몇개인지 구하기
total = 0

n = int(input())

num_len = len(str(n))

# 자리수 전까지 더하기
for i in range(1, num_len):
    total += i * 9 * (10 ** (i - 1))

# 현재 자리수 더하기
big = (n - (10 ** (num_len - 1)) + 1) * num_len
total += big

print(total)





