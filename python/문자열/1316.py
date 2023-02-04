# 1. 숫자를 입력받는다
# 2. 입력받은 숫자만큼 메서드(그룹단어체크)를 반복
# 2 - 1. 메서드-> 현재 단어랑 다음 단어가 같은지 체크
# 2 - 2. elif, 뒤의 인덱스 중 같은 단어가 있다면 그룹단어가 아님->break
# 3. 개수 출력

def group_word_check(word):
    for i in range(len(word) - 1):
        if (word[i] == word[i + 1]):
            pass
        elif (word[i] in word[i + 2:]):
            return -1
    return 0


n = int(input())
ans = n

for i in range(n):
    word = input()
    ans += group_word_check(word)

print(ans)
