import heapq, sys
input = sys.stdin.readline

population, height, trial = map(int, input().split())
trial_original = int(trial)
big = []


for _ in range(population):
    heapq.heappush(big, -int(input()))

while trial:
    if big[0] == -1:
        break
    if -big[0] < height:
        break
    biggest = -(heapq.heappop(big))
    half = biggest // 2
    heapq.heappush(big, -half)
    trial -= 1


if -big[0] < height:
    print("YES")
    print(trial_original -  trial)
else:
    print("NO")
    print(-big[0])

