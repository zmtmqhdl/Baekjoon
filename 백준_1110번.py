n = m = int(input()) # 값 대입
count = 0 # 결과값 카운트
while True : # False가 될 때까지 반복
    num1 = m // 10 # m의 앞자리 수
    num2 = m % 10 # m의 뒷자리 수
    new = num1 + num2 # 각 자리의 숫자를 더함
    m = int(str(num2) + str(new % 10)) # 문자로 더하기 위해 int형을 str로 변환하여 문자를 합친 후 다시 int형으로 변환
                                       # 기존 m의 뒷자리 수 + new의 뒷자리 수
    count += 1 # count = count + 1
    if m == n : # 조건문 if
        print(count) # 출력
        break # 반복문 멈춤