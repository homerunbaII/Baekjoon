
fibo_list = [0, 1]


n = int(input()) + 1
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    for i in range(2, n):
        result = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(result)
    print(fibo_list[-1])
