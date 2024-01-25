n = int(input())
pt = input()
pt_front = pt[0:pt.index('*')]
pt_end = pt[pt.index('*') + 1:]
pt_end_reverse = pt_end[::-1]



for _ in range(n):
    word = input()
    check = 0
    for i in range(len(pt_front)):
        if pt_front[i] != word[i]:
            check = 1
            break
    for i in range(len(pt_end)): # dc
        if pt_end_reverse[i] != word[len(word)-1-i]:
            check = 1
            break
    if check == 0 :
        print("DA")
    else:
        print("NE")