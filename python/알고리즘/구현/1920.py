n = int(input())
num_list = list(map(int, input().split()))

n_dict = {}

for i in num_list:
    n_dict[i] = 1

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_dict:
        print(1)
    else:
        print(0)