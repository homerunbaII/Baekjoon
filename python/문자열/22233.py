import sys

input= sys.stdin.readline

key_word, write = map(int,input().split())
key_dict = {}

for i in range(key_word):
    key = input().rstrip()
    key_dict[key] = 1


for i in range(write):
    write_list = input().rstrip().split(',')
    cnt = 0
    for j in write_list:
        if j in key_dict:
            key_dict[j] = 0
        else:
            pass
    for j in key_dict:
        if key_dict[j] == 1:
            cnt += 1
        else:
            pass
    print(cnt)