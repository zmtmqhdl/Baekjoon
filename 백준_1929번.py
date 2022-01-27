m, n = map(int, input().split()) # 값 대입
def isprime(m, n) : # 함수 생성
    n += 1 # n = n + 1
    data = [True] * n # True값을 가진 n개의 원소를 포함한 data라는 list생성
                      # data의 해당 인덱스 값이 True이면 소수, False이면 소수가 아님
    for i in range(2, int(n ** 0.5) + 1) : # 반복문 for -> n ** 0.5는 제곱근
        if data[i] == True : # 조건문 if
            for j in range(2 * i, n, i) : # 반복문 for -> 2 * i부터 n까지 i를 간격으로 j에 차례대로 대입
                data[j] = False
    for i in range(m, n) : # 반복문 for
        if i > 1 and data[i] == True : # 조건문 if -> 1은 소수가 아니므로 1 > 1
            print(i) # 출력   
isprime(m, n) # 함수 실행
# 에라토스테네스의 체