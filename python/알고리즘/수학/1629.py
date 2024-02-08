n, m , divide = map(int,input().split())

def power(a,b,c):
    if b == 0:
        print(1)
        return 1
    elif b % 2 == 0:
        y = power(a, b // 2, c)
        print(y)
        return (a*a) % c
    else:
        y = power(a, (b - 1), c)
        print(y)
        return (a *y * y) % c
    
print(power(n,m,divide))
