t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    n = int(input()) # 값 대입
    data = list(map(str, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
    for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
        if i == 0 : # 조건문 if, elif
            result = data[0] # result라는 변수를 data[0]값으로 초기화
        elif ord(data[i]) > ord(result[0]) : # ord를 사용하여 유니코드값을 비교
                                             # result[0]의 값과 data[i]의 값을 비교하여 data[i]의 값이 클 경우
            result = result + data[i] # data[i]를 뒤에 삽입
        elif ord(data[i]) <= ord(result[0]) : # ord를 사용하여 유니코드값을 비교
                                             # result[0]의 값과 data[i]의 값을 비교하여 data[i]의 값이 작을 경우
            result = data[i] + result # data[i]를 앞에 삽입
    print(result) # 출력