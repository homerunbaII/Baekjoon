# 1. 크로아티아 단어 입력받기
# 2. 크로아티아 알파벳 리스트 작성
# 3. 입력받은 단어 for문으로 순회하면서 알파벳 리스트 검증
# 4. 일치할 경우 replace 메서드를 통해 한글자 알파벳으로 바꾸기
# 5. 바꾼 단어의 개수를 len()으로 센 후 값 출력

cro_word = input()

cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_alp:
    cro_word = cro_word.replace(i, '0')


print(len(cro_word))
