n = int(input()) # 테스트 횟수 대입
plus = 0 # plus 초기화
score = 0 # socre 초기화
for _ in range(n) : # 반복문 for
    data = input() # 값 대입
    for i in range(len(data)) : # 반복문 for -> len(data)의 값만큼 반복
        if data[i] == 'O' : # 조건문 if, else
            plus += 1 # plus = plus + 1
            score += plus # score = socre + plus
        else :
            plus = 0 # plus 초기화
    print(score) # 출력
    score = 0 # score 초기화
    plus = 0 # plus 초기화