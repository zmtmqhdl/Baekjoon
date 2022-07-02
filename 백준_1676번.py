import math # 라이브러리 호출
n = int(input()) # 값 대입
n = str(math.factorial(n)) # factorial을 사용하여 n! 연산
count = 0 # 결과값을 저장할 count변수 초기화
for i in n[::-1] : # 반복문 for -> n의 마지막 문자부터 첫 문자까지 차례대로 i에 대입하며 반복
    if i != '0' : # 조건문 if -> i가 0이 아닌 경우
        break # 중지
    count += 1 # count = count + 1
print(count) # 출력