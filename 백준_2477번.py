k = int(input()) # 멜론의 개수
data = [] # data라는 list생성
for _ in range(6) : # 반복문 for -> 6번 반복
    x, y = map(int, input().split()) # 값 대입
    data.append([x, y]) # append를 사용하여 x, y를 2중 list형태로 data라는 list의 원소로 대입
w = 0 # 가로의 최대 길이를 저장할 변수 w초기화
w_idx = 0 # 가로의 최대 길이의 index값을 저장할 변수 w_idx초기화
h = 0 # 세로의 최대 길이를 저장할 변수 h초기호ㅘ
h_idx = 0 # 세로의 최대 길이를 index값을 저장할 변수 h_idx초기화
for i in range(6) : # 반복문 for -> 0부터 5까지 차례대로 i에 대입하며 반복
	if data[i][0] == 1 or data[i][0] == 2 : # 조건문 if -> 동, 서 방향일 경우
	    if w < data[i][1] : # 조건문 if -> w가 data[i][1]보다 작은 경우
	        w = data[i][1] # w에 data[i][1] 저장
	        w_idx = i # w의 index값을 w_idx에 저장
	elif data[i][0] == 3 or data[i][0] == 4 : # 조건문 if -> 남, 북 방향일 경우
	    if h < data[i][1] : # 조건문 if -> h가 data[i][1]보다 작은 경우
	        h = data[i][1] # h에 data[i][1] 저장
	        h_idx = i # h의 index값을 h_idx에 저장
w_sub = abs(data[(w_idx - 1) % 6][1] - data[(w_idx + 1) % 6][1]) # 작은 사각형의 가로 길이 연산
h_sub = abs(data[(h_idx - 1) % 6][1] - data[(h_idx + 1) % 6][1]) # 작은 사각형의 세로 길이 연산
result = ((w * h) - (w_sub * h_sub)) * k # (큰 사각형 넓이 - 작은 사각형 넓이) * 멜론의 개수 연산
print(result) # 출력