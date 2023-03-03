stack = []


def VPScheck(array, text):
    if text == '(':
        array.append(text)
    if text == ')':
        if not array:
            array.append('False')
            return
        array.pop()


t = int(input())

for i in range(t):
    text = input()
    for i in text:
        VPScheck(stack, i)
        if 'False' in stack:
            break
    if stack:
        print('NO')
    else:
        print('YES')
    stack = []
