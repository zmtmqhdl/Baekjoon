while True : # 반복문 for -> False가 반환될 때까지 반복
    a, b = map(int, input().split()) # 값 대입
    if a == 0 and b == 0 : # 조건문 if -> 마지막 줄에 0이 2개 주어진 경우
        break # 반복문 중지
    if b % a == 0 : # 조건문 if, elif, else -> 첫 번째 숫자가 두 번째 숫자의 약수인 경우
        print('factor') # 출력
    elif a % b == 0 : # 첫 번째 숫자가 두 번째 숫자의 배수인 경우
        print('multiple') # 출력
    else : # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아닌 경우
        print('neither') # 출력