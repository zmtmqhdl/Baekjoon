n, m = map(int, input().split()) # 값 대입
start_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] # 맨 왼쪽 위 칸이 B가 먼저 시작 되는 경우를 표현한 start_B라는 list생성
start_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] # 맨 왼쪽 위 칸이 W가 먼저 시작 되는 경우를 표현한 start_W라는 list생성
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n번 반복
    line = list(input()) # 대입된 값을 원소로 갖는 line이라는 list생성
    data.append(line) # append를 사용하여 data에 line을 원소로 대입
result = 64 # 8 * 8의 크기를 가진 체스판이므로 모든 칸을 수정한다고 가정할 때의 최대값을 가진 result변수 생성
for i in range(n - 7) : # 반복문 for -> 0부터 n - 8까지 i에 차례대로 대입하며 반복
                        # 8칸씩 잘라서 사용하므로 n - 7
    for j in range(m - 7) : # 반복문 for -> 0부터 n - 8까지 j에 차례대로 대입하며 반복
                            # 8칸씩 잘라서 사용하므로 m - 7
        start_B_count = 0 # 맨 왼쪽 위 칸을 B로 시작했을 때 수정해야하는 칸을 계산하는 start_B_count변수 생성
        start_W_count = 0 # 맨 왼쪽 위 칸을 W로 시작했을 때 수정해야하는 칸을 계산하는 start_W_count변수 생성
        for a in range(8) : # 반복문 for -> 0부터 7까지 a에 차레대로 대입하며 반복
                            # 8 * 8 크기의 체스판을 추출하는 과정
            for b in range(8) : # 반복문 for -> 0부터 7까지 b에 차례대로 대입하며 반복 
                                # 8 * 8 크기의 체스판을 추출하는 과정
                if data[i + a][j + b] != start_B[a][b] : # 조건문 if -> 맨 왼쪽 위 칸이 B로 시작했을 때의 연산
                    start_B_count += 1 # start_B_count = start_B_count + 1
                if data[i + a][j + b] != start_W[a][b] : # 조건문 if -> 맨 왼쪽 위 칸이 W로 시작했을 때의 연산
                    start_W_count += 1 # start_W_count = start_W_count + 1
        result = min(result, start_B_count, start_W_count) # min을 사용하여 result, start_B_count, start_W_count중에서 가장 작은 값을 result로 지정
print(result) # 출력