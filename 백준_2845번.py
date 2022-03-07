l, p = map(int, input().split()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
result = [] # 결과값을 저장할 result라는 list생성
for i in range(len(data)) : # 반복문 for -> 0부터 len(data) - 1까지 i에 차례대로 대입하며 반복
    result.append(data[i] - (l * p)) # append를 사용하여 data[i] - (l * p)값을 result라는 list에 대입
for i in result : # result라는 list의 원소를 차례대로 i에 대입
    print(i, end = ' ') # end를 사용하여 개행을 하지 않고 공백을 넣고 i값을 출력