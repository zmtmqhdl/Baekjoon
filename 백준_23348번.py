level = list(map(int, input().split())) # 대입된 값을 원소로 갖는 level이라는 list생성
n = int(input()) # 값 대입
data = [] # score라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    score = 0 # 동아리원의 점수를 저장할 변수score 초기화
    for _ in range(3) : # 반복문 for -> 3회 반복
        a = list(map(int, input().split())) # 대입된 값을 원소로 갖는 a라는 list생성
        for i in range(3) : # 반복문 for -> 0부터 2까지 i에 차례대로 대입하며 반복
            score += a[i] * level[i] # score = score + a[i] * level[i]
    data.append(score) # append를 사용하여 data라는 list에 score를 원소로 추가
print(max(data)) # max를 사용하여 data라는 list에서 가장 큰 값을 갖는 원소를 출력