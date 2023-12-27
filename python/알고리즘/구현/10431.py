import sys

p = int(input())

for i in range(p):
    test_list = list(map(int, sys.stdin.readline().split()))
    step = 0
    for i in range(1,21):
        for j in range(i + 1,21):
            if test_list[i] > test_list[j]:
                step +=1
    print(test_list[0], step)
