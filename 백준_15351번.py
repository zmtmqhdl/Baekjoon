n = int(input()) # 값 대입
for _ in range(n) : # 반복문 for -> n만큼 반복
    a = input() # 값 대입
    score = 0 # 점수를 저장할 score변수 초기화
    for i in a : # 반복문 for -> a에서 한 문자씩 i에 차례대로 대입하며 반복
        if i == ' ' : # 조건문 if -> 공백인 경우
            continue # 진행
        else : # 문자인 경우
            i_score = ord(i) - 64 # ord를 이용하여 점수 계산
            score += i_score # score = score + i_score
    if score == 100 : # 조건문 if -> score가 100인 경우
        print('PERFECT LIFE') # 출력
    else : # score가 100이 아닌 경우
        print(score) # 출력