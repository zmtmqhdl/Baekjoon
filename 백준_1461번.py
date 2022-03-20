n, m = map(int, input().split()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
plus = [] # 양수값을 저장할 data라는 list생성
minus = [] # 음수값을 저장할 data라는 list생성
move = 0 # 움직인 거리를 저장할 move변수 초기화
max_move = 0 # 제일 멀리 있는 책의 위치를 저장할 max_move변수 초기화
for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
    if i > 0 : # 조건문 if, elif -> i가 양수일 경우
        plus.append(i) # append를 사용하여 i를 plus라는 list의 원소로 추가 
    elif i < 0 : # i가 음수일 경우
        minus.append(i) # append를 사용하여 i를 minus라는 list의 원소로 추가
    if abs(i) > abs(max_move) : # 조건문 if -> abs을 사용하여 i와 max_move의 절댓값을 비교하여 i가 더 클 경우
        max_move = i # max_move 변경
plus.sort(reverse = True) # sort(reverse = True)를 사용하여 plus라는 list의 원소를 내림차순으로 정렬
minus.sort() # sort를 사용하여 minus라는 list의 원소를 오름차순으로 정렬
for i in range(0, len(plus), m) : # 반복문 for -> 0부터 len(plus) - 1까지 m을 간격으로 i에 대압히며 반복
    if plus[i] != max_move : # 조건문 if -> plus[i]의 값이 max_move와 같지 않을 경우
        move += plus[i] # move = move + plus[i]
for i in range(0, len(minus), m) : # 반복문 for -> 0부터 len(minus) - 1까지 m을 간격으로 i에 대입하며 반복
    if minus[i] != max_move : # 조건문 if -> mins[i]의 값이 max_move와 같지 않을 경우
        move += abs(minus[i]) # move = move + abs(minus[i])
move *= 2 # move = move * 2
          # 책을 놓고 제자리로 돌아오므로 move * 2
move += abs(max_move) # move = move + abs(max_move)
                      # 마지막 책을 놓고 제자리로 돌아오지 않는다.
print(move) # 출력