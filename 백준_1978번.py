n = int(input()) # 값 대입
data = list(map(int, input().split())) # 값 대입
result = 0 # 결과 초기화
for i in data : # 반복문 for -> data의 원소를 차례대로 i에 대입
    extra_count = 0 # 소수를 판별하기 위한 extra_count변수 초기화
    if i > 1 : # 조건문 if -> 1을 제외하기 위해서 i > 1
        for j in range(2, i) : # 반복문 for -> 2부터 i - 1까지 차례대로 j에 대입
            if i % j == 0 : # 조건문 if -> i가 소수가 아닐 경우
                extra_count = 1 # i가 소수가 아닐 경우
                break # 중지
        if extra_count == 0 : # 조건문 if -> i가 소수일 경우
            result += 1 # result = result + 1
print(result) # 출력