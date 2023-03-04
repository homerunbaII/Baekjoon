import sys

input = sys.stdin.readline

t = int(input())  # 테스트 케이스

for _ in range(t):
    new = int(input())  # 신입사원 수
    new_list = []  # 신입사원 리스트
    for _ in range(new):
        new_list.append(list(map(int, input().split())))  # 각자의 서류 성적과 면접 성적 입력
    count = 1
    new_list.sort(key=lambda x: x[0])  # 서류 성적 순위로 정렬
    min_grade = new_list[0][1]  # 4 면접 성적 최소 기준
    for i in range(len(new_list)):
        if min_grade > new_list[i][1]:  # 현재 면접최소성적보다 x높은성적(작은 숫자)가 나온다면
            min_grade = new_list[i][1]
            count += 1
    print(count)
