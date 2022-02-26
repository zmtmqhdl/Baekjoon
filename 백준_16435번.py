n, l = map(int, input().split()) # 값 대입
h = list(map(int, input().split())) # 대입된 값을 원소로 갖는 h라는 list생성
h.sort() # sort를 사용하여 h라는 list의 원소를 내림차순으로 정렬
while True : # 반복문 while -> False가 반환될 때까지 반복
    if len(h) != 0 and l >= h[0] : # 조건문 if, elif -> 스네이크가 먹을 수 있는 과일이 존재하는 경우
        del h[0] # h라는 list의 0번째 index에 저장된 값을 삭제
    elif len(h) == 0 or l < h[0]: # 스네이크버드가 더 이상 먹을 과일이 없거나 높이가 모자를 경우
        break # 중지
    l += 1 # l = l + 1
print(l) # 출력