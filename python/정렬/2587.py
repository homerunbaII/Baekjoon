num_list = []

for i in range(5):
    num_list.append(int(input()))

sorted_list = sorted(num_list)

print(sum(sorted_list) / 5)
print(sorted_list[2])
