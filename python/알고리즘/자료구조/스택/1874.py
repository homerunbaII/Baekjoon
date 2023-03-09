n = int(input())

pushpop = []
stack = []
temp = 0


for i in range(n):  # 1. 4 3 2
    x = int(input())
    if x > temp:  # 4 > 0
        for i in range(temp + 1, x+1):  # stack = [1,2,3,4]
            stack.append(i)
            pushpop.append('+')
        stack.pop()  # 4 pop
        pushpop.append('-')
        temp = x
    else:  # 3 < 4
        if stack[-1] == x:  # stack[-1] == 3
            stack.pop()  # stack.pop() = [1,2]
            pushpop.append('-')
        else:
            print('NO')
            break

if len(pushpop) == 2*n:
    for i in pushpop:
        print(i, end=' ')
