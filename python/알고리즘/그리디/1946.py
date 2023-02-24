import sys

input = sys.stdin.readline

t = int(input())  # 테스트 케이스

for _ in range(t):
    new = int(input())  # 신입사원 수
    new_list = []  # 신입사원 리스트
    for _ in range(new):
        new_list.append(list(map(int, input().split())))  # 각자의 서류 성적과 면접 성적 입력
    count = 0
    new_list.sort(key=lambda x: x[0])
    min_grade2 = new_list[0][1]  # 4 면접 성적 최소 기준
    new_list.sort(key=lambda x: x[1])
    min_grade1 = new_list[0][0]  # 4 서류 성적 최소 기준
    for i in new_list:  # new list 검사
        if (i[0] <= min_grade1 and i[1] <= min_grade2):
            count += 1
    print(count)
