import heapq as h

for _ in range(int(input())):
    n = int(input())
    file = list(map(int, input().split()))
    files = []
    total_cost = 0
    ## 최소 힙 
    for i in file:
        h.heappush(files, i)
    print(files)
    while len(files) > 1:
        file_1 = h.heappop(files)
        file_2 = h.heappop(files)
        new_file = file_1 + file_2
        print(file_1, file_2 ,new_file)
        h.heappush(files, new_file)
        total_cost += new_file
    print(files, total_cost)
    