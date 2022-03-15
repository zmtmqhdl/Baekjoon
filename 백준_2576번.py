data = [] # data라는 list생성
for _ in range(7) : # 반복문 for -> 7회 반복
    num = int(input()) # 값 대입
    if num % 2 == 1 : # 조건문 if -> num이 홀수인 경우
        data.append(num) # append를 사용하여 num을 data라는 list의 원소로 대입
if len(data) == 0 : # 조건문 if -> 홀수가 없는 경우
    print(-1) # 출력
else : # 홀수가 존재하는 경우
    print(sum(data)) # sum을 사용하여 data라는 list의 원소의 합을 출력
    print(min(data)) # min을 사용하여 data라는 list의 원소 중 최솟값 출력