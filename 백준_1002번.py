t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # 값 대입
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) # 조규현과 백승환 사이의 거리
    data = [r1, r2, distance] # r1, r2, distacne를 원소르 갖는 data라는 list생성
    m = max(data) # max를 사용해서 data라는 list에서 가장 큰 값을 가진 원소를 m이라는 변수로 지정
    data.remove(m) # append를 사용해서 data라는 list에서 m을 제거
    if distance == 0 and r1 == r2 : # 조건문 if, elif, else -> 마린의 위치 조사
                                    # 조규현과 백승환이 같은 위치에 있는 경우
        print(-1) # 출력
    elif distance == r1 + r2 or m == sum(data) : # 조규현의 범위와 백승환의 범위가 1개의 점에서만 겹칠 경우
        print(1) # 출력
    elif m > sum(data) : # 조규현의 범위와 백승환의 범위가 만나지 않을 경우
        print(0) # 출력
    else : # 조규현의 범위와 백승환의 범위가 2개의 점에서 겹칠 경우
        print(2) # 출력