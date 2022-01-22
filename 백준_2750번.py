t = int(input()) # 테스트 횟수 대입
data = [] # data라는 list 생성
for _ in range(t) : # 반복문 for -> t만큼 반복
    n = int(input()) # 값 대입
    if n not in data : # 가정문 if -> data라는 list에 n이라는 원소가 존재하지 않는다면
        data.append(n) # append를 사용하여 data라는 list에 n을 원소로 추가
data.sort() # sort를 사용하여 data라는 list를 오름차순으로 정렬
for i in data : # 반복문 for -> i에 data라는 list의 원소를 하나씩 대입
    print(i) # 출력