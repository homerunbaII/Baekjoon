h ,w  = map(int,input().split())

for i in range(h):
    cloud = input()
    cloud_cnt = 0
    cloud_first_checker = 0
    for i in range(w):
        if cloud[i] == '.':
            if cloud_first_checker == 0:
                print(-1, end = ' ')
            else:
                print(cloud_cnt, end = ' ')
                cloud_cnt += 1
        if cloud[i] =='c':
            cloud_cnt = 0
            print(cloud_cnt, end = ' ')
            cloud_cnt += 1
            cloud_first_checker = 1
        if i == w -1 :
            print('')
