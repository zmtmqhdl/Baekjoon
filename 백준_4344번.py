n = int(input()) # 테스트 횟수 대입
for _ in range(n) : # 반복문 for
    data = list(map(int, input().split())) # data라는 list에 int형을 값 대입
    average = sum(data[1:]) / data[0] # 평균값 연산
                                      # data[1:] -> data라는 list에서 1번 인덱스 ~ 마지막 인덱스까지라는 뜻
    count = 0 # count 초기화
    for score in data[1:] : # 반복문 for -> score라는 값에 data라는 list에서 1번째 인덱스 값부터 들어감
        if score > average : # 조건문 if
                count += 1 # count = count + 1
    result = count / data[0] * 100 # 결과 연산
    print(f'{result:.3f}%') # f-string을 사용하여 소수 3번재 자리까지 출력
                            # print(f'{값:.표현할 소수 자릿수f}') -> 표현할 소수 자릿수까지 소수점 표현