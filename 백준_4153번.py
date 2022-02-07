while True : # 반복문 while -> False가 반환될 때까지 반복
    a = list(map(int, input().split())) # 값 대입
    high = max(a) # 가장 큰 값을 high라는 변수로 지정
    if sum(a) == 0 : # 조건문 if -> 0 0 0이 입력된 경우
        break # 중지
    a.remove(high) # remove를 사용해 high값을 a라는 list에서 제거
    if high ** 2 == a[0] ** 2 + a[1] ** 2 : # 피타고라스의 정리 연산
        print("right") # 출력
    else :
        print("wrong") # 츨력
