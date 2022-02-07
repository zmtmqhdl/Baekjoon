def isPrime() : # 함수 생성
    data = [False, False] + [True] * 9999 # data라는 list 생성
                                          # 0, 1번째 index의 값은 False이고 그 이후의 값들은 True
                                          # data의 해당 인덱스 값이 True이면 소수, False이면 소수가 아님
    for i in range(2, int(10001 ** 0.5) + 1) : # 반복문 for -> 10001 ** 0.5는 제곱근
        if data[i] == True : # 조건문 if -> 소수 판별
            for j in range(2 * i, 10001, i) : # 반복문 for -> 2 * i부터 10001까지 i를 간격으로 j에 차례대로 대입
                data[j] = False
    t = int(input()) # 테스트 횟수 대입
    for _ in range(t) : # 반복문 for -> t만큼 반복
        n = int(input()) # 값 대입
        a = n // 2 # 두 소수의 차이를 가장 작게 하기 위해서 n // 2 
        b = n // 2 # 두 소수의 차이를 가장 작게 하기 위해서 n // 2
        for _ in range(10000) : # 반복문 for
            if data[a] == True and data[b] == True: # 조건문 if -> a와 b가 소수인지 판별
                print(a, b) # 출력
                break # 중지
            a -= 1 # a = a - 1
            b += 1 # b = b + 1
                   # a는 1증가시키고 b는 1감소시키면 a + b = n 성립
isPrime() # 함수 실행
