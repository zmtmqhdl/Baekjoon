n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(input())) # data라는 list에 값 대입
data.sort() # sort를 사용하여 data라는 list를 오름차순으로 정렬
for i in data : # 반복문 for -> i에 data라는 list의 원소를 하나씩 대입
    print(i) # 출력