n = input()
temp = n
stack = []
bracket = []
bin_list = []
ans = []


def bin_num(x):
    return x[2:]


for i in range(len(n)):
    if n[i] == '(':
        stack.append(i)
    if n[i] == ')':
        bracket.append([stack.pop(), i])

for i in range(2**len(bracket)):
    bin_list.append(bin_num(bin(i)).zfill(len(bracket)))

bin_list.pop()

for i in range(2**len(bracket) - 1):  # 0 ~ 7
    for j in range(len(bracket)):  # 0 ~ 2
        if bin_list[i][j] == '0':
            n = list(n)
            n[bracket[j][0]] = 'F'
            n[bracket[j][1]] = 'F'
    ans.append(n)
    n = temp

remove_set = {'F'}

for i in range(len(ans)):
    ans[i] = [j for j in ans[i] if j not in remove_set]


for i in range(len(ans)):
    ans[i] = ''.join(ans[i])

ans = set(ans)
ans = list(ans)
ans.sort()
for i in ans:
    print(i)
