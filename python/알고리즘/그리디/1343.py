# n = input()

# cnt = 0
# ABlist =[]

# for i in range(len(n)):
#     if n[i] == 'X':
#         cnt += 1
#         if i == len(n) - 1:
#             ABlist.append(cnt)
#     elif n[i] == '.' and cnt > 0:
#         ABlist.append(cnt)
#         cnt = 0
#         ABlist.append('.')
#     elif n[i] == '.' and cnt == 0:
#         ABlist.append('.')

# checker = 0

# for i in ABlist:
#     for j in ABlist:
#         if type(j) == int:
#             if j % 2 != 0:
#                 print(-1)
#                 checker = 1
#                 break
#     if checker == 1: 
#         break
#     if type(i) == int:
#         if i % 4 == 0:
#             print('AAAA' * (i // 4), end= '') 
#         else:
#             print('AAAA' * (i // 4), end= '') 
#             print('BB', end= '')
#     else:
#         print(i, end = '')


n = input()

n.replace('XXXX','AAAA')
n.replace('XX', 'BB')

if 'X' in n:
	print(-1)
else:
	print(n)