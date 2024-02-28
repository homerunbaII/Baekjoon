# 음수 채널 없음
def dfs(n, lst, length):
    if n == length:
        result.append(list(map(str,lst)))
    else:
        for i in good:
            dfs(n + 1, lst +[i], length)

def dfs2(n, lst, length):
    if n == length:
        result_2.append(list(map(str,lst)))
    else:
        for i in good:
            dfs2(n + 1, lst +[i], length)

def dfs3(n, lst, length):
    if n == length:
        result_3.append(list(map(str,lst)))
    else:
        for i in good:
            dfs3(n + 1, lst +[i], length)

def mini(result, length, small):
    for i in result:
            click = length
            num = int(''.join(i))
            click += abs(channel - num)
            small = min(small, click)
            print(click)
    return small

channel  = int(input())
length = len(str(channel))
# 머릿수
head = int(str(channel)[0])

m = int(input())
broke = []

if m != 0:
    broke = list(map(int, input().split()))

# 최소값은 100에서 +,- 만으로 이동한 값으로 갱신하고 시작
small = abs(channel - 100)

# 살아있는 숫자
good  = []
for i in range(10):
    if i not in broke:
        good.append(i)

if m == 10:
    print(small)
else:
    result = []
    dfs(0, [], length)
    small = mini(result, length, small)
    if length > 1 :
        result_2 = []
        dfs2(0, [], length -1)
        small = mini(result_2, length - 1, small)
    result_3 = []
    dfs3(0, [], length + 1)
    small = mini(result_3, length + 1, small)
    print(small)
    
