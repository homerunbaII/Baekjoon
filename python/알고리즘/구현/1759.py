from itertools import permutations, combinations
l,c = map(int, (input().split()))
 
word = list(input().split())

word_all = list(combinations(word, l))
word_possi = []

for i in word_all:
    m_cnt = 0
    z_cnt = 0
    for j in i:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            m_cnt += 1
        else:
            z_cnt += 1
    if m_cnt >=1 and z_cnt >= 2:
        word_possi.append(list(i))
        

for i in word_possi:
    i.sort()

word_possi.sort()

for i in word_possi:
    print(''.join(i))
    