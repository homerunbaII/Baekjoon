n = input()
check = 0


for i in range(int(len(n)/2)):
    if n[i] == n[-i-1]:
        pass
    else:
        print(n[i], n[-i])
        check = 1

if check == 1:
    print(0)
else:
    print(1)