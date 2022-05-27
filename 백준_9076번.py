t = int(input()) # 값 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
    data.remove(max(data)) # remove와 max를 사용하여 data라는 list에서 가장 큰 값의 원소를 제거
    data.remove(min(data)) # remove와 min을 사용하여 data라는 list에서 가장 작은 값의 원소를 제거
    if max(data) - min(data) >= 4 : # 조건문 if -> 최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상인 경우
        print('KIN') # 출력
    else : # 최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 3점 이하인 경우
        print(sum(data)) # 출력