while True : # 반복문 while -> False가 반환될 때까지 반복
    try : # 예외처리문 try, catch -> 정상적으로 작동할 경우
        print(input()) # 대입된 값 출력
    except : # 예외가 발생했을 경우
        break # 중지