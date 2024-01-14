from itertools import permutations

n = int(input())
number_list = [str(i) for i in range(1,10)]
all = list(permutations(number_list, 3))

for i in range(n):
    guess, strike ,ball = map(int, input().split())
    guess = list(str(guess))
    remove_cnt = 0
    for i in range(len(all)):
        s, b = 0, 0
        i -= remove_cnt
        for j in range(3):
            if all[i][j] == guess[j]:
                s += 1
            elif guess[j] in all[i]:
                b += 1
        if  s != strike or b != ball:
            all.remove(all[i])
            remove_cnt += 1

print(len(all))