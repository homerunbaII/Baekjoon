n = int(input())
main = list(input())
answer = 0

for i in range(n -1):
    main_compare = main[:]
    word = input()
    cnt = 0
    for j in word:
        if j in main_compare:
            main_compare.remove(j)
        else:
            cnt += 1

    if cnt < 2 and len(main_compare) < 2:
        answer += 1
 
print(answer)

