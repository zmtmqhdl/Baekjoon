data = str(input()) # 값 대입
time = 0 # 결과값을 저장할 time변수 초기화
letter = 'A' # 시작 문자 저장할 letter변수에 'A'저장
for i in data : # 반복문 for -> data라는 문자를 한 문자씩 차례대로 i에 대입하며 반복
    left = ord(letter) - ord(i) # ord를 사용하여 문자를 유니코드로 변경
                                # 왼쪽으로 돌리는 경우
    right = ord(i) - ord(letter) # ord를 사용하여 문자를 유니코드 변경
                                 # 오른쪽으로 돌리는 경우
    if left < 0 : # 조건문 if -> left가 0보다 작은 경우
        left += 26 # left = left + 26
    if right < 0 : # 조건문 if -> right가 0보다 작은 경우
        right += 26 # right = right + 26
    letter = i # letter변수 변경
    time += min(right, left) # min을 활용하여 right, left 중에서 작은 값을 찾음
                             # time = time + min(right, left)
print(time) # 출력