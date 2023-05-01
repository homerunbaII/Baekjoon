char = input()
new_char = ''
temp_char = ''

flag = 0

for i in range(len(char)):
    if flag == 0 and char[i] == ' ':
        new_char += temp_char[::-1]
        temp_char = ''
    if char[i] == '<':
        flag = 1
        new_char += temp_char[::-1]
        temp_char = ''
    if flag == 1:
        new_char += char[i]
    if flag == 0:
        if char[i] == ' ':
            new_char += ' '
        else:
            temp_char += char[i]
    if char[i] == '>':
        flag = 0

new_char += temp_char[::-1]


print(new_char)
