n = int(input()) # 테스트 횟수 대입
result = 0 # 결과값을 저장할 result변수 초기화
plus = [] # 양수를 저장할 plus라는 list생성
minus = [] # 음수와 0을 저장할 minus라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data = int(input()) # 값 대입
    if data == 1 : # 조건문 if, elif -> data가 1일 경우는 무조건 더해야 함
        result += 1 # result = result + 1
    elif data > 0  : # data가 양수인 경우
        plus.append(data) # append를 사용하여 data를 plus라는 list의 원소로 대입
    elif data <= 0 : # data가 음수 또는 0인 경우
        minus.append(data) # append를 사용하여 data를 minus라는 list의 원소로 대입
plus.sort() # sort를 사용하여 plus라는 list를 오름차순으로 정렬
minus.sort() # sort를 사용하여 minus라는 list를 내림차순으로 정렬
if len(plus) % 2 == 1 : # 조건문 if, elif -> plus라는 list의 원소의 개수가 홀수인 경우
    result += plus[0] # result = result + plus[0] -> 가장 작은 수를 result에 더함
    del plus[0] # 가장 작은 수를 plus라는 list에서 제거
    for i in range(0, len(plus), 2) : # 반복문 for -> 0부터 len(plus) - 1까지 2를 간격으로 두고 i에 차례대로 대입하며 반복
        result += plus[i] * plus[i + 1] # result = result + (plus[i] * plus[i + 1]) -> 2개씩 묶어서 곱한 후 result에 더함
elif len(plus) % 2 == 0 : # plus라는 list의 원소의 개수가 짝수인 경우
    for i in range(0, len(plus), 2) : # 반복문 for -> 0부터 len(plus) - 1까지 2를 간격으로 두고 i에 차례대로 대입하며 반복
        result += plus[i] * plus[i + 1] # result = result + (plus[i] * plus[i + 1]) -> 2개씩 묶어서 곱한 후 result에 더함
if len(minus) % 2 == 1 : # 조건문 if, elif -> minus라는 list의 원소의 개수가 홀수인 경우
    result += minus[-1] # result = result + minus[0] -> 가장 작은 수를 result에 더함
    del minus[-1]  # 가장 작은 수를 minus라는 list에서 제거
    for i in range(0, len(minus), 2) : # 반복문 for -> 0부터 len(minus) - 1까지 2를 간격으로 두고 i에 차례대로 대입하며 반복
        result += minus[i] * minus[i + 1] # result = result + (minus[i] * minus[i + 1]) -> 2개씩 묶어서 곱한 후 result에 더함
elif len(minus) % 2 == 0 : # minus라는 list의 원소의 개수가 짝수인 경우
    for i in range(0, len(minus), 2) : # 반복문 for -> 0부터 len(minus) - 1까지 2를 간격으로 두고 i에 차례대로 대입하며 반복
        result += minus[i] * minus[i + 1] # result = result + (minus[i] * minus[i + 1]) -> 2개씩 묶어서 곱한 후 result에 더함
print(result) # 출력