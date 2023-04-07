def g(n):
    if n <= 1:
        return n
    else:
        return (5 * g(n-1) - 6 * g(n - 2))


print(g(1))
print(g(2))
print(g(3))
print(g(4))
print(g(5))
print(g(6))
print(g(7))

27 - 8
81 - 16
243 - 32
729 - 64
