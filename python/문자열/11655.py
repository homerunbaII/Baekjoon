from string import ascii_lowercase, ascii_uppercase


n = input()



for i in n:
    if i in ascii_uppercase:
        index =  ascii_uppercase.find(i)
        index += 13
        if index > 25:
            index = index % 26
        print(ascii_uppercase[index], end='')
    elif i in ascii_lowercase:
        index =  ascii_lowercase.find(i)
        index += 13
        if index > 25:
            index = index % 26
        print(ascii_lowercase[index], end='')
    else:
        print(i, end='')