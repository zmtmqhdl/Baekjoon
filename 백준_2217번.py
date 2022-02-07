n = int(input()) # 테스트 회수 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(input())) # data라는 list에 대입된 값을 원소로 추가
data.sort(reverse = True) # sort(reverse = True)를 사용하여 data라는 list를 내림차순으로 정렬
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    data[i] = data[i] * (i + 1) # 
print(max(data)) # max를 사용하여 data라는 list에서 최댓값을 출력