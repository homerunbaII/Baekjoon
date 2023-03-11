import sys

stick = sys.stdin.readline().rstrip()

stack = ['(']
total = 0

for i in range(1, len(stick)):
    if stick[i] == '(':
        stack.append(stick[i])
    if stick[i - 1] == '(' and stick[i] == ')':
        stack.pop()
        total += len(stack)
    if stick[i - 1] == ')' and stick[i] == ')':
        stack.pop()
        total += 1

print(total)
