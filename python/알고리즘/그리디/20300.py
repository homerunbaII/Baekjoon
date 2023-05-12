n = int(input())
machine = list(map(int, input().split()))

machine.sort()


def find_max(machine):
    max_val = 0
    for i in range(len(machine)//2):
        temp = machine[i] + machine[len(machine)-1-i]
        if (temp > max_val):
            max_val = temp
    return max_val


if len(machine) % 2 == 0:
    result = find_max(machine)
    print(result)
else:
    big = machine.pop()
    result = find_max(machine)
    if result > big:
        print(result)
    else:
        print(big)
