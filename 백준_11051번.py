import sys # 라이브러리 호출
import math # 라이브러리 호출
n, k = map(int, sys.stdin.readline().split()) # 값 대입
result = factorial(n) // (factorial(k) * factorial(n - k)) # 결과값 연산
print(result % 10007) # 출력