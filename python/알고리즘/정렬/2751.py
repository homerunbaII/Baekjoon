
# array = []

# n = int(input())

# for i in range(n):
#     array.append(int(input()))


# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:  # 피벗보다 큰 데이터를 찾을 때까지
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때까지
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]  # 이 이후 종료
#         else:
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)


# quick_sort(array, 0, len(array) - 1)

# print(array)
import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

for i in sorted(array):
    print(i)
