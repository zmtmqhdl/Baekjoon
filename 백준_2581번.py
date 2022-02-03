m = int(input()) # 값 대입
n = int(input()) # 값 대입
data = [] # data라는 list생성
for i in range(m, n + 1) : # 반복문 for -> m부터 n까지의 값을 i에 차례대로 대입
    count = 0 # 소수를 판별하기 위한 count변수 초기화
    if i > 1 : # 조건문 if -> 1을 제외하기 위해서 i > 1
        for j in range(2, i) : # 반복문 for -> 2부터 i - 1까지 차레대로 j에 대입
            if i % j == 0 : # 조건문 if -> i가 소수가 아닐 경우
                count = 1 # i가 소수가 아닐 경우
                break # 중지
        if count == 0 : # 조건문 if -> i가 소수일 경우
            data.append(i) # data라는 list에 i를 원소로 추가
if len(data) > 0 : # 조건문 if -> 소수가 있을 경우와 없을 경우를 판단
    print(sum(data)) # sum을 활용해 data라는 list에 있는 원소의 합을 출력
    print(min(data)) # min을 활용해 data라는 list에 있는 원소들 중 최소값을 출력
else : 
    print(-1) # 출력