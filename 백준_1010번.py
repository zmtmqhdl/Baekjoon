import math # 라이브러리 호출
t = int(input()) # 값 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    n, m = map(int, input().split()) # 값 대입
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m - n)) # 결과값을 저장할 result변수에 결과를 연산하여 저장
    print(result) # 출력