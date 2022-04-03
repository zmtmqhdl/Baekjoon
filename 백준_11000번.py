import heapq # 라이브러리 호출
import sys
n = int(sys.stdin.readline()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    s, t = map(int, sys.stdin.readline().split()) # 값 대입
    data.append([s, t]) # append를 사용하여 data라는 list에 [s, t]를 원소로 대입
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
room = [] # room이라는 list생성
heapq.heappush(room, data[0][1]) # heqppush를 사용하여 room이라는 list에 data[0][1]을 원소로 대입
for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 i에 차례대로 대입
    if data[i][0] < room[0] : # 조건문 if, else -> 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠른 경우
        heapq.heappush(room, data[i][1]) # heappush를 사용하여 data[i][1]의 값을 room이라는 list에 대입 -> 새로운 회의실 개설
    else : # 현재 회의가 끝나고 이어서 회의가 개최 가능한 경우
        heapq.heappop(room) # heappop을 사용하여 room이라는 list에서 가장 작은 원소값 제거
        heapq.heappush(room, data[i][1]) # heappush를 사용하여 data[i][1]의 원소를 room이라는 list에 대입
print(len(room)) # room이라는 list의 원소 개수 출력