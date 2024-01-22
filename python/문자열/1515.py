n = input()

num = 0
while len(n):
    num += 1
    num_str = str(num)
    while len(num_str) and len(n):
        if num_str[0] == n[0]:
            n = n[1:]
        num_str = num_str[1:]

print(num)
    



# n = input()

# number_dict = {}
# count_dict = {}
# for i in range(0, 10):
#     number_dict[i] = 0

# for i in n:
#     number_dict[int(i)] += 1

# # while True:
# #     for i in 
# num = 1

# while True:
#     count_dict = {}
#     for i in range(0, 10):
#         count_dict[i] = 0
#     print(count_dict)
#     print(num)
#     for i in range(1, num + 1):
#         for j in str(i):
#             count_dict[int(j)] += 1
#     print(count_dict)
#     checker = 0
#     for i in range(0, 10):

#         print('n', number_dict[i],'j', count_dict[i])
#         if number_dict[i] > count_dict[i]:
#             checker = 1
#             break
#     print(checker, 'chchc')
#     if checker == 0:
#         break
#     num += 1

# print(num)
    
        
        

