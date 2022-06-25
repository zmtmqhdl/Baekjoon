n, q = map(int, input().split()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(input())) # append를 사용하여 data라는 list에 대입된 값을 원소로 추가
for _ in range(q) : # 반복문 for -> q만큼 반복
    t = int(input()) # 값 대입
    for i in range(n) : # 반복문 for -> 0부터 n - 1까지 차례대로 i에 대입하며 반복
        if t < sum(data[:i + 1]) : # 조건문 if -> t가 sum(data[:i + 1])보다 작은 경우
            print(i + 1) # 출력
            break # 중지