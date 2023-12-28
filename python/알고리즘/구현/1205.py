n, t_score, p = map(int, input().split())
if n > 0:
    rank_list = list(map(int, input().split()))
    rank = 1
    for i in range(n):
        if t_score > rank_list[i]:
            print(rank)
            break
        elif t_score == rank_list[i]:
            if t_score <= rank_list[n - 1] and  n == p:
                print(-1)
                break
            else:
                print(rank)
                break
        else:
            rank += 1
        if rank == (n + 1) and n == p:
            print(-1)
            break
        elif rank == (n + 1) and p > n:
            print(rank)
else:
    print(1)

