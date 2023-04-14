left_list = {'q': (1, 3), 'w': (2, 3), 'e': (3, 3), 'r': (4, 3), 't': (5, 3),
             'a': (1, 2), 's': (2, 2), 'd': (3, 2), 'f': (4, 2), 'g': (5, 2),
             'z': (1, 1), 'x': (2, 1), 'c': (3, 1), 'v': (4, 1), }

right_list = {'y': (1, 3), 'u': (2, 3), 'i': (3, 3), 'o': (4, 3), 'p': (5, 3),
              'h': (1, 2), 'j': (2, 2), 'k': (3, 2), 'l': (4, 2),
              'b': (0, 1), 'n': (1, 1), 'm': (2, 1)}

sec = 0

l_start, r_start = input().split()

char = input()

for i in char:
    if i in left_list:
        sec += abs(left_list[l_start][0] - left_list[i][0])
        sec += abs(left_list[l_start][1] - left_list[i][1])
        l_start = i
        sec += 1
    if i in right_list:
        sec += abs(right_list[r_start][0] - right_list[i][0])
        sec += abs(right_list[r_start][1] - right_list[i][1])
        r_start = i
        sec += 1

print(sec)
