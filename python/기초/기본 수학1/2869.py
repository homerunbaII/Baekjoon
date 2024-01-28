# 나무의 높이 V미터
# 낮에 A미터 - 밤에 B 미터
# 1. V, A, B를 입력받는다
# 2. 높이 변수 h를 선언해준다,
# 3. h +=A와 h -=B를 반복해주어 h가 V를 넘는 순간 break한다.

# a, b, v = map(int, input().split())  # 5 1 6
# h = 0
# cnt = 1

# while (cnt):
#     h += a
#     if (h >= v):
#         break
#     h -= b
#     cnt += 1

# print(cnt)


# 다른 방법
# 1. a-b의 값을 구한다
# 2. v 에서 a를 뺀 다음 a-b로 나눈 후 1을 더해준다
import math
a, b, v = map(int, input().split())  # 9 7 18
one_day_up = a - b  # 2
result = math.ceil((v - a) / one_day_up) + 1  # v - a = 9 ### 2 4 6 8 10 19
print(result)
