n = int(input()) # 값 대입
result = 0 # 결과값을 저장할 result변수 생성
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지의 값을 i에 차례대로 대입하며 반복
    data = list(map(int, str(i))) # str(i)의 값을 int형으로 바꿔 한 문자씩을 원소로 갖는 data라는 list생성
    result = i + sum(data) # i와 i를 이루는 각 자리수의 합
    if result == n : # 조건문 if -> 생성자 조건에 해당된다면
        print(i) # 출력
        break # 중지
    if i == n : # 조건문 if -> 생성자가 존재하지 않을 경우
        print(0) # 출력