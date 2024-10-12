import sys, itertools

input = sys.stdin.readline

word_dic = {}

while True:
    word = input().rstrip()
    if word == '-':
        break
    word_dic[word] = 1

while True:
    puzzle =input().rstrip()
    if puzzle == '#':
        break
    puzzle_dic = {}
    alphabet_dic = {}
    puzzle = list(puzzle)
    for i in range(4,10):
        combination = list(itertools.combinations(puzzle, i))
        # 4 ~ 9개의 조합
        for comb in combination:
            permutation = list(itertools.permutations(comb,i))
            for perm in permutation:
                perm = ''.join(perm)
                if perm in word_dic:
                    if perm not in puzzle_dic:
                        puzzle_dic[perm] = 1
    for i in puzzle:
        if i not in puzzle_dic:
            alphabet_dic[i] = 0
    for dic_word in puzzle_dic:
        dic_word = set(dic_word)
        for k in dic_word:
            alphabet_dic[k] +=1
    
    print_list = []

    for i in alphabet_dic:
        print_list.append([i,alphabet_dic[i]])
    print_list.sort(key = lambda x : (x[1], x[0]))

    small = print_list[0][1]
    big = print_list[-1][1]
    min_list =[]
    max_list = []
    for i in print_list:
        if i[1] == small:
            print(i[0], end = '')
        else:
            break
    print(' '+ str(small), end = ' ')
    for i in print_list:
        if i[1] == big:
            print(i[0], end = '')
    print(' '+ str(big))
    
    
    