data = [] # data라는 list생성
for _ in range(5) : # 반복문 for -> 5회 반복
    n = int(input()) # 값 대입
    if n < 40 : # 조건문 if -> n이 40미만일 경우
        n = 40 # n의 값을 40으로 저장
    data.append(n) # append를 사용하여 data라는 list에 n의 값을 원소로 대입
print(int(sum(data) / 5)) # 평균 출력