paper = int(input())

sheet = [[0] * 100 for _ in range(100)]

for i in range(paper):
    x , y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            sheet[y+ k][x + j] = 1

colored = 0

for i in sheet:
    for j in i:
        if j == 1:
            colored += 1

print(colored)


