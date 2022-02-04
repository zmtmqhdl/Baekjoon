n = int(input()) # 테스트 횟수 대입
data = [] # data라는 list생성
for _ in range(n): # 반복문 for -> n만큼 반복
    x, y = map(int, input().split()) # 값 대입
    data.append((x, y)) # append를 사용하여 x, y를 data라는 list의 원소로 대입
for i in data: # 반복문 for -> i에 data의 원소를 차례대로 대입
    rank = 1 # 순위 초기화
    for j in data: # 반복문 for -> j에 data의 원소를 차례대로 대입
        if i[0] < j[0] and i[1] < j[1]: # 조건문 if -> i의 x, y의 값이 j의 x, y값보다 작을 경우
                                        # i보다 j의 덩치가 큰 경우
                rank += 1 # rank = rank + 1
    print(rank, end = " ") # end를 사용하여 개행없이 출력