stack = []

n = list(input())
ans = 0
tmp = 1

for i in range(len(n)):  # (()[[]])([])
    if n[i] == '(':
        stack.append(n[i])
        tmp *= 2
    elif n[i] == '[':
        stack.append(n[i])
        tmp *= 3
    elif n[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if n[i-1] == '(':
            ans += tmp
        tmp //= 2
        stack.pop()
    elif n[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if n[i-1] == '[':
            ans += tmp
        tmp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)
