import heapq # 라이브러리 호출
n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    heapq.heappush(data, int(input())) # heappush를 사용하여 data라는 list에 대입된 값을 원소로 추가하면서 정렬
if len(data) == 1 : # 조건문 if, else -> 카드 묶음이 1개인 경우
    print(0) # 출력
else : # 카드 묶음이 여러 개인 경우
    result = 0 # 결과값을 저장할 result변수 초기화
    while len(data) > 1 : # 반복문 while -> 카드 묶음이 2개 이상인 경우
        min1 = heapq.heappop(data) # heappop을 이용하여 data라는 list에서 가장 작은 값을 min1으로 지정하고 제거
        min2 = heapq.heappop(data) # heappop을 이용하여 data라는 list에서 가장 작은 값을 min2으로 지정하고 제거
        result += min1 + min2 # result = result + (min1 + min2)
        heapq.heappush(data, min1 + min2) # heappush를 이용하여 data라는 list에 min1 + min2의 값을 원소로 추가하면서 정렬ㄴ
    print(result) # 출력