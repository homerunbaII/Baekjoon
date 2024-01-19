from string import ascii_lowercase

n = int(input())

number_list = []

for i in range(n):
    letter = input()
    start = 0
    num = []
    for j in range(len(letter)):
        if letter[j] in ascii_lowercase:
            if start == 1:
                while num[0] == '0' and len(num) > 1:
                    num.pop(0)
                number_list.append(''.join(num))
                num = []
            start = 0
        else:
            start = 1
            num.append(letter[j])
            if j == len(letter) - 1:
                while num[0] == '0' and len(num) > 1:
                    num.pop(0)
                number_list.append(''.join(num))
                num = []

number_list = list(map(int, number_list))
number_list.sort()

for i in number_list:
    print(i)

# from string import ascii_lowercase

# n = int(input())

# number_list = []

# for i in range(n):
#     letter = input()
#     start = 0
#     num = []
#     for j in range(len(letter)):
#         if letter[j] in ascii_lowercase:
#             if start == 1:
#                 checker_0 = 1
#                 for k in num:
#                     if k != '0':
#                         checker_0 = 0
#                         break
#                 if checker_0 == 0:
#                     while num[0] == '0':
#                         num.pop(0)
#                     number_list.append(''.join(num))
#                     num = []
#                 else:
#                     num = []
#             start = 0
#         else:
#             start = 1
#             num.append(letter[j])
#             if j == len(letter) - 1:
#                 checker_0 = 1
#                 for k in num:
#                     if k != '0':
#                         checker_0 = 0
#                         break
#                 if checker_0 == 0:
#                     while num[0] == '0':
#                         num.pop(0)
#                     number_list.append(''.join(num))
#                     num = []
#                 else:
#                     num = []

# number_list = list(map(int, number_list))
# number_list.sort()

# for i in number_list:
#     print(i)
