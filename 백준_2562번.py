data = [] # list 생성
for _ in range(9) : # 반복문 for -> 괄호 안에 있는 수만큼 반복
    data.append(int(input())) # data라는 list에 값 대입
print(max(data)) # 최댓값 출력
print(data.index(max(data)) + 1) # data라는 list에서 최댓값의 인덱스 값 + 1 -> 인덱스는 0부터 시작