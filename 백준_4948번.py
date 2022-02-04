num = 123456 * 2 + 1 # n의 최대범위 + 1 -> list생성을 위한 변수
data = [True] * num # True값을 가진 num개의 원소를 갖는 data라는 list생성
                    # data의 해당 인덱스 값이 True이면 소수, False이면 소수가 아님
for i in range(2, int(num ** 0.5) + 1) : # 반복문 for -> num ** 0.5는 제곱근
    if data[i] == True : # 조건문 if -> 소수 판별
        for j in range(2 * i, num, i) : # 반복문 for -> 2 * i부터 num까지 i를 간격으로 j에 차례대로 대입
            data[j] = False
def prime_count(n) : # 함수 생성
    count = 0 # 소수 개수를 계산하기 위해 count변수 초기화
    for i in range(n + 1, n * 2 + 1) : # 반복문 for
        if data[i] == True : # 조건문 if -> i가 소수라면
            count += 1 # count = count + 1
    print(count) # 출력
while True : # 반복문 while -> False가 반환될 때까지 반복
    n = int(input()) # 값 대입
    if n == 0 : # 조건문 if
        break # 중지
    prime_count(n) # pirme_count함수에 n대입
#에라토스테네스의 체