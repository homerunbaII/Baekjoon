fibo_list = [0, 1]

n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n+1):
        result = fibo_list[i-1] + fibo_list[i-2]
        fibo_list[i] = (result)
    print(fibo_list[-1])
