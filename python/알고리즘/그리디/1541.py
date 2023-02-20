# def deletezero(array):
#     while (array[0] == '0'):
#         del array[0]
#     index = 0
#     for i in array:
#         if i in ['+', '-', '(']:
#             while (array[index + 1] == '0'):
#                 del array[index + 1]
#         index += 1
#     return array


# soosik = list(input())  # 55-50+40
# indexnum = 0

# for i in soosik:  # 5, 5, -
#     if i == '-':  # -
#         soosik.insert(indexnum + 1, '(')  # 3번째 위치에 insert
#         j = indexnum  # 3
#         while (True):
#             j += 1  # 4번째 index 55-
#             if (soosik[j] == '-'):
#                 soosik.insert(j, ')')
#                 break
#             if (j == len(soosik) - 1):
#                 soosik.insert(j + 1, ')')
#                 indexnum += 1
#                 break
#     indexnum += 1

# soosik = deletezero(soosik)
# result = ''.join(soosik)

# print(eval(result))

soosik = list(input().split('-'))
sum = 0

for i in soosik[0].split('+'):  # 첫번째 '-'가 나오기 전까지의 합
    sum += int(i)

for i in soosik[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
