def calculate_minimum_switches(numbers):
    # 세그먼트 정의
    segments = {
        0: set("abcdef"),
        1: set("bc"),
        2: set("abdeg"),
        3: set("abcdg"),
        4: set("bcfg"),
        5: set("acdfg"),
        6: set("acdefg"),
        7: set("abc"),
        8: set("abcdefg"),
        9: set("abcdfg")
    }
    
    # 주어진 숫자들의 세그먼트 찾기
    all_segments = [segments[number] for number in numbers]
    
    # 모든 세그먼트의 공통 부분 찾기
    common_segments = set.intersection(*all_segments) if all_segments else set()
    
    # 공통 세그먼트를 제외한 나머지 세그먼트 찾기
    unique_segments = set.union(*all_segments) - common_segments if all_segments else set()
    
    # 필요한 스위치 개수 계산
    switch_count = len(common_segments) + len(unique_segments)
    return switch_count

# 예시 입력
numbers_example = [1,2]

# 최소 스위치 개수 계산
minimum_switches = calculate_minimum_switches(numbers_example)
print(minimum_switches)