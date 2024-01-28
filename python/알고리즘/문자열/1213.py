name = input()
f_dict = {}

# 딕셔너리에 입력값 추가
for i in name:
    f_dict[i] = 0

for i in name:
    f_dict[i] += 1

# 홀수 개가 있는지 검사
cnt = 0
temp = 0
for i in f_dict:
    if f_dict[i] % 2 != 0:
        cnt += 1
        temp = i
        f_dict[temp] -= 1
    if cnt > 2:
        break

f_dict = sorted(f_dict.items())
word = []

if cnt <= 1:
    if cnt == 1:
        middle = temp
    for i in f_dict:
        fre = i[1] // 2
        for j in range(fre):
            word.append(i[0])
    if cnt == 0:
        print(''.join(word)+ ''.join(word[::-1]))
    if cnt == 1:
        print(''.join(word)+ middle+ ''.join(word[::-1]))
elif cnt > 1:
    print('I\'m Sorry Hansoo')

