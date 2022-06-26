t = int(input()) # 값 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    x1, y1, x2, y2 = map(int, input().split()) # 값 대입
    n = int(input()) # 값 대입
    result = 0 # 결과값을 저장할 result변수 초기화
    for _ in range(n) : # 반복문 for -> n만큼 반복
        px, py, radius = map(int, input().split()) # 값 대입
        start = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5 # 행성중심부터 시작점까지의 거리
        end = (((px - x2) ** 2) + ((py - y2) ** 2)) ** 0.5 # 행성중심부터 도착점까지의 거리
        if start < radius and end < radius : # 조건문 if, elif -> 시작점과 도착점이 모두 원 안에 있을 경우
            pass #  # 통과
        elif start < radius : # 시작점이 안에 있을 경우
            result += 1 # result = result + 1
        elif end < radius : # 도착점이 안에 있을 경우
            result += 1 # result = result + 1
    print(result) # 출력