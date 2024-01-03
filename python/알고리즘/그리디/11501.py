test = int(input())
for i in range(test):
    day = int(input())
    price_list = list(map(int, input().split()))
    max_price = max(price_list)

    profit = 0
    if price_list[0] == max_price:
        print(0)
        continue
    else:
        j = 0
        while j < day:
            if price_list[j] < max_price:
                profit += (max_price - price_list[j])
            if price_list[j] == max_price and j < day - 1:
                max_price = max(price_list[j + 1:])
            j += 1
        print(profit)



