a, b = map(int, input().split()) # 값 대입
n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(input())) # append를 사용하여 입력된 값을 data라는 list의 원소로 추가
b_plus = b_minus = b # b의 값을 1씩 증감시켜 변형해갈 b_plus, b_minus변수 생성
while True : # 반복문 while -> False가 반환될 때까지 반복
    if b_plus == a or b_minus == a : # 조건문 if, elif -> b_plus, b_minus의 값이 a와 같을 경우
        print(abs(b - a)) # abs를 사용하여 b - a에 값에 절댓값을 적용 후 출력
        break # 중지
    elif b_plus in data : # b_plus의 값이 data라는 list에 존재하는 경우
        print(b_plus - b + 1) # 출력
        break # 중지
    elif b_minus in data : # b_minus의 값이 data라는 list에 존재하는 경우
        print(b - b_minus + 1) # 출력
        break # 중지
    b_plus += 1 # b_plus = b_plus + 1
    b_minus -= 1 # b_minus = b_minus - 1