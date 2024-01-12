import sys

input = sys.stdin.readline


n, m = map(int, input().split())
chess_board = []
result = []

for i in range(n):
    chess_board.append(input().rstrip())

print(chess_board)


for i in range(n - 7):
    for j in range(m - 7):
        check1 = 0
        check2 = 0
        for a in range(i ,i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if chess_board[a][b] == 'B' : 
                        check1 += 1
                    if chess_board[a][b] == 'W' :
                        check2 += 1
                else:
                    if chess_board[a][b] == 'B' :
                        check2 += 1
                    if chess_board[a][b] == 'W' :
                        check1 += 1
        result.append(min(check1, check2))

print(min(result))
                        



