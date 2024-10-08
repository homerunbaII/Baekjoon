from string import ascii_lowercase

n = int(input())

shortcut = {}

for i in ascii_lowercase:
    shortcut[i] = 0
    shortcut[i.upper()] = 0
    
for i in range(n):
    option = input()
    # 단어장 만들기
    option_list = option.split()
    flag = 0
    flag_2 = 0
    for j in option:
        if shortcut[j] == 0:
            flag = 1
            break
        if shortcut[j.upper()] == 0:
            flag = 1
            break
    if flag == 0:
        print(option)
        continue
    for j in range(len(option_list)):
        # 첫글자가 단축키 등록이 안되어 있을 때
        if shortcut[option_list[j][0]] == 0 : 
            flag_2 = 1
            shortcut[option_list[j][0]] = 1
            shortcut[option_list[j][0].upper()] = 1
            print(f'[{option_list[j][0]}]{option_list[j][1:]}', end = ' ')
            for k in range(j + 1, len(option_list)):
                print(option_list[k], end = ' ')
            break
    if flag_2 == 0: 
        for j in range(len(option)):
            if j == ' ':
                print(' ', end = '')
                continue
            temp = option[j].lower()
            if shortcut[temp] == 0:
                shortcut[temp] = 1
                shortcut[temp.upper()] = 1
                print(f'[{option[j]}]{option[j + 1:]}')
                break
            else:
                print(option[j], end = '')




