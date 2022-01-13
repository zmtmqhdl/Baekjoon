data = [] # 빈 list 생성
for _ in range(10) : # 반복문 for
    n = int(input()) # 값 대입
    if n % 42 not in data : # data라는 list에 n % 42의 값이 없다면 
        data.append(n % 42) # n % 42의 값을 data라는 list에 대입
print(len(data)) # data라는 list 안에 담겨 있는 원소의 갯수 출력