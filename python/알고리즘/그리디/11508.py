import sys

quantity = int(sys.stdin.readline())
price_list = []

for i in range(quantity):
    price_list.append(int(sys.stdin.readline()))

price_list.sort(reverse= True)

total_price = 0

for i in range(len(price_list)):
    if i % 3 == 0:
        total_price += price_list[i]
    elif i % 3 == 1:
        total_price += price_list[i]
    else:
        pass

print(total_price)