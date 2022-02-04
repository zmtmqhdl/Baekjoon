n = int(input()) # 값 대입
count = 0 # count 초기화
num = 666 # 666이 들어간 가장 첫 번째 숫자를 값으로 가진 변수 num생성
while True : # 반복문 While -> False가 반복될 때까지 반복
    if '666' in str(num) : # 조건문 if -> str(num)에 666이 포함되어있을 경우
        count += 1 # count = count + 1
    if count == n : # 조건문 if -> count가 n과 값이 같을 경우
        print(num) # 출력
        break # 중지
    num += 1 # num = num + 1