from string import ascii_lowercase

n = int(input())

name_dict = {}

for i in ascii_lowercase:
    name_dict[i] = 0

for i in range(n):
    name = input()
    first_letter = name[0]
    name_dict[first_letter] += 1

checker = 0

for i in name_dict:
    if name_dict[i] >= 5:
        checker = 1
        print(i, end= '')
    else:
        pass

if checker == 0:
    print('PREDAJA')
    
