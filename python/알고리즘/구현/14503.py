n , m = map(int, input().split())

x, y, direction = map(int, input().split())

room_condition = []
clean_count = 0

for i in range(n):
    room_condition.append(list(map(int,input().split())))


while True:
    if room_condition[x][y] == 0:
        room_condition[x][y] = -1
        clean_count += 1
    if room_condition[x - 1][y] != 0 and room_condition[x][y - 1] != 0 and room_condition[x + 1][y] != 0 and room_condition[x][y + 1] != 0:
        if direction == 0 and room_condition[x + 1][y]  != 1:
            x += 1
            continue
        elif direction == 1 and room_condition[x][y - 1]  != 1:
            y -= 1
            continue
        elif direction == 2 and room_condition[x - 1][y]  != 1:
            x -= 1
            continue
        elif direction == 3 and room_condition[x][y + 1]  != 1:
            y += 1
            continue
        else: 
            break

    if room_condition[x - 1][y] == 0 or room_condition[x][y - 1] == 0 or room_condition[x + 1][y] == 0 or room_condition[x][y + 1] == 0:
        while True:
            if direction == 3 or direction == 2 or direction == 1:
                direction -= 1
            elif direction == 0 :
                direction = 3
            if direction == 0 and room_condition[x - 1][y]  == 0:
                x -= 1
                break
            elif direction == 1 and room_condition[x][y + 1]  == 0:
                y += 1
                break
            elif direction == 2 and room_condition[x + 1][y]  == 0:
                x += 1
                break
            elif direction == 3 and room_condition[x][y - 1]  == 0:
                y -= 1
                break

print(clean_count)

