x = int(input()) # 값 대입
n = int(input()) # 값 대입
result = 0 # 결과값을 저장할 result변수 초기화
for _ in range(n) : # 반복문 for -> n만큼 반복
    a, b = map(int, input().split()) # 출력
    result += a * b # result = result + (a * b)
if result == x : # 조건문 if, else -> 영수증 계산이 정확한 경우
    print("Yes") # 출력
else : # 영수증 출력이 부정확한 경우
    print("No") # 출력