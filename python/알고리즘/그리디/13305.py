# city_num = int(input())
# city_dis = list(map(int, input().split()))
# city_oilprice = list(map(int, input().split()))

# total_price = city_dis[0] * city_oilprice[0]
# cur_price = city_oilprice[0]
# cur_dis = 0

# for i in range(1, city_num - 1):  # 맨처음 도시는 앞에서 더해주었고, 마지막 도시는 가격이 영향을 미치지 않음
#     if cur_price > city_oilprice[i]:  # 현재 가격이 다음도시 가격보다 비싸다면
#         total_price += cur_dis * cur_price  # 지금까지 쌓인 미터 * 현재 가격 정산
#         cur_price = city_oilprice[i]  # 새로운 싼 가격
#         cur_dis = city_dis[i]  # 다음 도시까지의 거리
#     else:
#         cur_dis += city_dis[i]  # 거리만 추가
#     if (i == city_num - 2):  # 마지막 도시 전 정산
#         total_price += cur_dis * cur_price


# print(total_price)

city_num = int(input())
city_dis = list(map(int, input().split()))
city_oilprice = list(map(int, input().split()))

price = city_oilprice[0]
total = 0

for i in range(city_num - 1):
    if (price > city_oilprice[i]):
        price = city_oilprice[i]
    total += city_dis[i] * price

print(total)
