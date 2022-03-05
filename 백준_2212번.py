n = int(input()) # 값 대입
k = int(input()) # 값 대입
data = sorted(list(map(int, input().split()))) # 대입된 값을 원소로 갖는 data라는 생성
                                               # sorted를 사용해 대입된 원소를 오름차순으로 정렬
if k >= n : # 조건문 if, else -> 집중국의 수가 센서보다 많을 경우
    print(0) # 출력
else :
    dist = [] # dist라는 list생성
    for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 i에 차례대로 대입하며 반복
        dist.append(data[i] - data[i - 1]) # append를 사용하여 data[i] - data[i - 1]값을 dist라는 list의 원소로 대입
    dist.sort(reverse = True) # sort(reverse = True)를 사용하여 dist라는 list의 원소를 내림차순으로 정렬
    for _ in range(k - 1) : # 반복문 for -> k - 2번 반복
        dist.pop(0) # pop을 사용하여 0번째 index의 값을 dist라는 list에서 제거
    print(sum(dist)) # sum을 사용하여 dist라는 list의 원소의 합을 출력