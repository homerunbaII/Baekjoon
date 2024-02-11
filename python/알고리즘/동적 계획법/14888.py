from itertools import permutations

n = int(input())
num_list= list(map(int,input().split()))
plus, minus, multi, divide = map(int,input().split())
operator = ['+' for _ in range(plus)] + ['-' for _ in range(minus)] + ['*' for _ in range(multi)] + ['/' for _ in range(divide)]
per = list(set(permutations(operator, n-1)))

result = []

for i in per:
    start = num_list[0]
    for j in range(0, n - 1):
        if i[j] == '+':
            start += num_list[j + 1]
        if i[j] == '-':
            start -= num_list[j + 1]
        if i[j] == '*':
            start *= num_list[j + 1]
        if i[j] == '/':
            if start < 0:
                start = -start
                start //= num_list[j + 1]
                start = -start
            else:
                start //= num_list[j + 1]
    result.append(start)



print(max(result))
print(min(result))