import sys # 라이브러리 호출
n = int(sys.stdin.readline()) # 값 대입
A, B = 100, 100 # 시작 점수
for _ in range(n) : # 반복문 for -> n만큼 반복
    a, b = map(int, input().split()) # 값 대입
    if a > b : # 조건문 if, elif -> a가 b보다 큰 경우
        B -= a # B = B - a
    elif a < b : # a가 b보다 작은 경우
        A -= b # A = A = A - b
print(A, B, sep = "\n") # 출력