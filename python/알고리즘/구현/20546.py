# def sungmin(m, price_list):
#     stock = 0  # 주식개수
#     cnt = [0, 0]  # 0번째 index는 몇일 연속인지, 1번째 index는 상승인지 하강인지
#     tmp = price_list[0]
#     for i in range(0, len(price_list)):
#         if price_list[i] > tmp:  # 전날보다 높을 때
#             if cnt[1] == 1:  # 전날도 상승장
#                 cnt[0] += 1  # 연속 상승 일수 + 1
#             else:  # 상승장이 아니었을 때
#                 cnt[0] = 1  # 연속 상승 일수 = 1일차
#                 cnt[1] = 1  # 상승장
#         elif price_list[i] == tmp:  # 전날하고 동일할 때
#             cnt[0] = 0  # 초기화
#             cnt[1] = 0  # 초기화
#         else:  # 전날보다 낮을 때
#             if cnt[1] == -1:  # 전날도 하락장
#                 cnt[0] -= 1  # 연속 하락 일수 - 1
#             else:  # 하락장이 아니었을 때
#                 cnt[0] = -1  # 연속 하락 일수 1일차
#                 cnt[1] = -1  # 하락장
#         if (cnt[0] >= 3):  # 3일 연속 상승장일 때
#             m += price_list[i] * stock  # 매도하고 남은 돈
#             stock = 0  # 0주
#         if (-3 >= cnt[0]):  # 3일 연속 하락장일 때
#             stock += m // price_list[i]  # 매수
#             m %= price_list[i]  # 매수하고 남은 돈
#         tmp = price_list[i]

#     m += stock * price_list[13]  # 마지막날 주가
#     return m

def junhyun(m, price_list):
    stock = 0
    for i in price_list:
        stock += m // i
        m %= i
    m += stock * price_list[13]
    return m


def sungmin(m, price_list):
    stock = 0
    for i in range(len(price_list) - 4):
        if price_list[i] > price_list[i+1] > price_list[i+2] > price_list[i+3]:  # 3일연속 감소한다면
            stock += m // price_list[i+3]
            m %= price_list[i+3]
        if price_list[i] < price_list[i + 1] < price_list[i+2] < price_list[i+3]:  # 3인 연속 상승한다면
            m += price_list[i+3] * stock
            stock = 0
    m += price_list[-1] * stock
    return m


m = int(input())  # 돈
price_list = list(map(int, input().split()))  # 14일치 주가

m_j = junhyun(m, price_list)
m_s = sungmin(m, price_list)

if (m_j > m_s):
    print("BNP")
elif m_j < m_s:
    print("TIMING")
else:
    print("SAMESAME")
