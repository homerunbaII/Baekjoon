screen , basket = map(int, input().split())
apple = int(input())

basket_location = [i + 1 for i in range(basket)]
distance = 0

for i in range(apple):
    apple_location = int(input())
    if apple_location in basket_location:
        continue
    elif apple_location < basket_location[0]:
        while apple_location not in basket_location:
            for j in range(len(basket_location)):
                basket_location[j] -= 1
            distance += 1
        continue
    elif apple_location > basket_location[-1]:
        while apple_location not in basket_location:
            for j in range(len(basket_location)):
                basket_location[j] += 1
            distance += 1
        continue

print(distance)


