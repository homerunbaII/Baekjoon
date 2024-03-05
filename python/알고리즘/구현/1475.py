a = list(map(int, list(input())))

num_dict = {}

for i in range(10):
    num_dict[i] = 0

for i in a:
    if i == 9:
        i = 6
    num_dict[i] += 1


if num_dict[6] % 2 == 0:
    num_dict[6] //= 2
else:
    num_dict[6] = (num_dict[6] + 1) // 2


b =num_dict.values()
    

print(max(b))