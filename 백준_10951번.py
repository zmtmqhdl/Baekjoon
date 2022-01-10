while True :  # False가 될 때까지 반복
    try : # 예외 처리 try, except -> try는 실행시킬 코드
        a, b = map(int, input().split()) # 값 대입
        print(a + b) # 출력
    except : # a, b에 int형이 아닌 다른 값이 들어가면 실행시킬 코드
             # try부번에서 오류 발생시 실행시킬 코드
        break # 반복문 멈춤