import heapq # 라이브러리 호출
import sys # 라이브러리 호출
n, k = map(int, sys.stdin.readline().split()) # 값 대입
gem = [] # 보석 정보를 저장할 gem이라는 list생성
bag = [] # 가방 정보를 저장할 bag이라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    m, v = map(int, sys.stdin.readline().split()) # 값 대입
    heapq.heappush(gem, [m, v]) # heappush를 사용하여 gem이라는 list에 [m, v]를 원소로 대입하고 정렬
for _ in range(k) : # 반복문 for -> k만큼 반복
    c = int(sys.stdin.readline()) # 값 대입
    heapq.heappush(bag, c) # heappush를 사용하여 bag이라는 list에 c를 원소로 대입하고 정렬
result = 0 # 결과값을 저장할 result변수 초기화
select_gem = [] # 가방의 무게보다 작은 보석들의 정보를 저장할 select_gem이라는 list생성
for _ in range(k) : # 반복문 for -> k만큼 반복
    select_bag = heapq.heappop(bag) # heappop을 이용하여 bag이라는 list에서 가장 작은 값을 삭제 후 그 값을 select_bag에 저장
    while gem and select_bag >= gem[0][0] : # 반복문 while -> gem이라는 list에 원소가 1개 이상 있고 select_bag의 값이 gem의 무게보다 같거나 큰 경우 반복
        [m, v] = heapq.heappop(gem) # heappop을 이용하여 gem이라는 list에서 가장 작은 값을 삭제 후 그 값을 [m, v]에 저장
        heapq.heappush(select_gem, -v) # heappush를 이용하여 select_gem이라는 list에 -v값을 대입 -> max heap
    if select_gem : # 조건문 if, elif -> select_gem이라는 list의 원소가 1개 이상일 경우
        result -= heapq.heappop(select_gem) # result = result - (select_gem이라는 list에서 가장 큰 값 -> 음수 형태)
    elif not gem : # gem이라는 list의 원소가 없을 경우
        break # 중지
print(result) # 출력