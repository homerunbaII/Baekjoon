n = int(input())
sum = input()

stack = []
num_list = []

for i in range(n):
    num_list.append(int(input()))


for i in range(len(sum)):
    if sum[i].isalpha():
        code = ord(sum[i]) - ord('A')
        stack.append(num_list[code])
    if sum[i] in '*+/-':
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(str(a)+sum[i]+str(b)))

print('%.2f' % stack[0])
