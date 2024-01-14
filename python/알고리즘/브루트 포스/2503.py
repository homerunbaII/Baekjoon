from itertools import permutations

n = int(input())

guess_list = []
all_list = [i for i in range(100,1000)]

for i in range(n):
    guess, strike ,ball = map(int, input().split())
    guess = str(guess)
    num_100 = int(guess[0])
    num_10 = int(guess[1])
    num_1 = int(guess[2])
    guessnum_list= [num_100, num_10, num_1]
    number_list = [i for i in range(1,10)]
    if strike == 0 and ball == 0:
        for i in guessnum_list:
            number_list.remove(i)
        data = permutations(number_list, 3)
        for i in data:
            all_list.remove(i[0] * 100 + i[1] * 10 + i[2])
    if strike == 1 and ball == 0:
        pass
    if strike == 0 and ball == 1:
        pass
    if strike == 1 and ball == 1:
        pass
    if strike == 2 and ball == 0:
        pass
    if strike == 0 and ball == 2:
        pass
    if strike == 1 and ball == 2:
        pass
    if strike == 2 and ball == 1:
        pass

print(all_list)