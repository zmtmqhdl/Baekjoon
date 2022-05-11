n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    a, b = map(int, input().split()) # 값 대입
    data.append([a, b]) # data라는 list에 [a, b]를 원소로 추가
data.sort(key = lambda x : (x[0], x[1])) # sort(key = lambda x : (x[0], x[1]))
time = data[0][0] + data[0][1] # 소가 입장하는데 걸리는 시간을 저장하기 위한 변수 time생성
                               # 처음 입장하는 소의 시간을 time변수에 저장
for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 i에 차례대로 대입하며 반복
    if time >= data[i][0] : # 새로 도착한 소의 도착시간보다 기존의 소들이 입장한 시간보다 작은 경우 
        time += data[i][1] # time = time + data[i][1]
                           # 기존의 시간 + 새로 도착한 소의 검수 시간
    else : # 새로 도착한 소의 도착시간이 기존의 소가 검수받고 입장한 시간보다 큰 경우
        time = data[i][0] + data[i][1] # time변수 변경
print(time) # 출력