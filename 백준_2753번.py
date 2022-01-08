year = int(input()) # 값 대입
if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0 : # 조건문 if, else를 사용하고 나눗셈의 나머지 연산 %, 값이 같지 않다는 연산 != 사용한다. 그리고를 뜻하는 and연산, 또는을 뜻하는 or연산
    print(1) # 출력
else :
    print(0)