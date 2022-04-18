v = int(input()) # 값 대입
cute = 0 # 1이 나온 횟수를 저장할 cute변수 초기화
for _ in range(v) : # 반복문 for -> v만큼 반복
    if int(input()) == 1 : # 조건문 if -> 대입된 값이 1일 경우
        cute += 1 # cute = cute + 1
if cute > v // 2 : # 조건문 if, else -> 1이 나온 횟수가 0보다 많을 경우
    print("Junhee is cute!") # 출력
else : # 1이 나온 횟수보다 0이 나온 횟수가 더 많을 경우
    print("Junhee is not cute!") # 출력