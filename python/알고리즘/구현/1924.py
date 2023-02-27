mon, date = map(int, input().split())

monthdate = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 1 ~ 12월 날짜
dayofweek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
totalday = date

if (mon == 1):
    pass
else:
    for i in range(mon - 1):
        totalday += monthdate[i]  # 총 날짜 수

mod = totalday % 7  # 나머지
print(dayofweek[mod])
