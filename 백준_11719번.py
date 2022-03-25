while True : # 반복문 while -> False가 반환될 때까지 반복
    try : # 정상적으로 실행할 경우
        print(input()) # 입력된 값을 출력
    except EOFError : # 예외가 발생할 경우
        break # 중지