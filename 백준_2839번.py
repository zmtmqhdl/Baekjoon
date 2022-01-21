n = int(input()) # 값 대입
result = 0
while True: # 반복문 while -> True가 False가 될 때까지 반복
    if (n % 5) == 0: # 조건문 if -> 만약 n이 5로 나눴을 때 나머지가 0이라면
        result = result + (n // 5) # result = result + (n // 5) -> result에 n을 5로 나눴을 때의 몫을 더함
        print(result) # 출력
        break # 중지
    n -= 3 # n = n -3
    result += 1 # result = result + 3
    if n < 0: # 조건문 if -> 만약 n이 0보다 작다면
              # n이 3과 5로 나누어떨이지지 않는 경우
        print(-1) # 출력
        break # 중지