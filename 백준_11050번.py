import math # 라이브러리 호출
n, k = map(int, input().split()) # 값 대입
result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) # 결과값을 저장할 result변수 생성
print(result) # 출력