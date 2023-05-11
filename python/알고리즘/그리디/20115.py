n = int(input())
energy_list = list(map(int, input().split()))

max_en = max(energy_list)
energy_list.remove(max(energy_list))
total = sum(energy_list) * 0.5 + max_en

print(total)
