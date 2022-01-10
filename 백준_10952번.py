while True : # False가 될 때까지 반복
    a, b = map(int, input().split()) # 값 대입
    if a == 0 and b == 0 : # 조건문 if, else
        break # 반복문 멈춤
    else :
        print(a + b) # 출력