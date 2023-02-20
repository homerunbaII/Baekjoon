pay = int(input())
changes = 1000 - pay

coin_list = [500, 100, 50, 10, 5, 1]
coin_cnt = 0
for i in coin_list:
    coin_cnt += changes // i
    changes %= i

print(coin_cnt)
