import random

def simulate_missions(participants, total_time, success_probs, times_per_stage, wait_times):
    stages = [0] * participants  # 모든 참가자는 1단계(0)에서 시작
    results = [0] * participants  # 각 참가자의 최종 위치
    total_time_spent = [0] * participants  # 각 참가자가 소요한 총 시간
    
    for minute in range(total_time):
        for i in range(participants):
            if stages[i] == 3:  # 졸업한 참가자
                continue  # 졸업한 참가자는 더 이상 미션을 수행하지 않음
            
            if total_time_spent[i] >= total_time:
                continue  # 시간이 남아있지 않으면 더 이상 진행하지 않음
            
            # 현재 단계
            current_stage = stages[i]
            
            # 현재 단계에 필요한 시간 (수행 시간 + 대기 시간)
            current_stage_time = times_per_stage[current_stage] + wait_times[current_stage]
            
            # 성공 확률 체크
            if random.random() < success_probs[current_stage]:
                stages[i] += 1  # 성공 시 다음 단계로 진급
                total_time_spent[i] += current_stage_time  # 사용한 시간 추가
            else:
                stages[i] = max(0, stages[i] - 1)  # 실패 시 이전 단계로 강등
                total_time_spent[i] += current_stage_time  # 사용한 시간 추가
            
            results[i] = stages[i]  # 현재 위치 업데이트
    
    return results, total_time_spent

# 초기 설정
participants = 16
total_time = 50 * 2  # 총 50분을 30초 단위로 환산
success_probs = [0.25, 0.20, 0.15]  # 각 단계별 성공 확률
times_per_stage = [1, 2, 4]  # 각 단계 소요 시간 (30초 단위)
wait_times = [2, 2, 6]  # 각 단계 대기 시간 (30초 단위)

num_simulations = 100  # 시뮬레이션 반복 횟수

# 시뮬레이션 결과 누적
graduated_total = 0
stage_3_total = 0
stage_2_total = 0
stage_1_total = 0
all_times_to_graduate = []  # 졸업한 모든 참가자의 소요 시간을 저장
fastest_times_list = []  # 가장 빨리 졸업한 참가자의 소요 시간을 저장

for _ in range(num_simulations):
    final_results, total_time_spent = simulate_missions(participants, total_time, success_probs, times_per_stage, wait_times)
    
    stages_count = [final_results.count(stage) for stage in range(4)]  # 각 단계별 인원수 집계
    graduated_total += stages_count[3]
    stage_3_total += stages_count[2]
    stage_2_total += stages_count[1]
    stage_1_total += stages_count[0]
    
    # 졸업한 참가자의 소요 시간 저장
    times_to_graduate = [total_time_spent[i] for i in range(participants) if final_results[i] == 3]
    all_times_to_graduate.extend(times_to_graduate)
    
    # 가장 빨리 졸업한 참가자의 소요 시간 찾기
    if times_to_graduate:
        fastest_times_list.append(min(times_to_graduate))

# 평균 계산
graduated_avg = graduated_total / num_simulations
stage_3_avg = stage_3_total / num_simulations
stage_2_avg = stage_2_total / num_simulations
stage_1_avg = stage_1_total / num_simulations
avg_time_to_graduate = sum(all_times_to_graduate) / len(all_times_to_graduate) if all_times_to_graduate else 0
avg_fastest_time_to_graduate = sum(fastest_times_list) / len(fastest_times_list) if fastest_times_list else 0

print(f"100번 시뮬레이션의 평균 결과:")
print(f"졸업한 참가자 팀 평균: {graduated_avg:.2f}")
print(f"3단계에서 끝난 참가자 팀 평균: {stage_3_avg:.2f}")
print(f"2단계에서 끝난 참가자 팀 평균: {stage_2_avg:.2f}")
print(f"1단계에서 끝난 참가자 팀 평균: {stage_1_avg:.2f}")
print(f"졸업한 참가자의 평균 소요 시간: {avg_time_to_graduate * 30 / 60:.2f} 분")
print(f"가장 빨리 졸업한 참가자의 평균 소요 시간: {avg_fastest_time_to_graduate *30 / 60:.2f} 분")
