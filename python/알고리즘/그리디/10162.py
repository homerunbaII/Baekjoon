sec = int(input())
button_cnt = []

button = [300, 60, 10]

if (sec % 10 != 0):
    button_cnt.append(-1)
else:
    for i in button:
        button_cnt.append(sec // i)
        sec = sec % i

for i in button_cnt:
    print(i, end=' ')
