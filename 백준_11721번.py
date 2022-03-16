data = input() # 값 대입
while True : # 반복문 while -> False가 반환될 때까지 반복
    if len(data) <= 10 : # len(data)의 길이가 10이하일 경우
        print(data) # 출력
        break # 중지
    else : # len(data)의 길이가 11이상인 경우
        print(data[:10]) # 1부터 10번째 index문자값 출력
        data = data[10:] # 출력한 문자를 제외한 문자들을 data로 정의