n = int(input()) # 값 대입
data = [] # data라는 list생성
result = 0 # 결과값을 저장할 result변수 초기화
schedule = [False] * 1001 # False값을 1001개 가진 schedule이라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    d, w = map(int, input().split()) # 값 대입
    data.append((d, w)) # append를 사용하여 (d, w)를 data라는 list의 원소로 대입
data.sort(key = lambda x : x[1], reverse = True) # sort(key = lambda, reverse = True)를 사용해서 data라는 list의 원소를 점수를 기준으로 내림차순으로 정렬
for day, score in data : # 반복문 for -> data라는 list의 원소를 day, score에 대입하며 반복
    i = day # 마감일을 확인하기 위한 변수i에 day저장
    while i > 0 and schedule[i] == True : # 반복문 while -> i가 양수이고 schedule[i]가 True인 경우
                                          # scheduel[i]의 값이 False이면 과제 가능
        i -= 1 # i = i - 1
               # 마감일이 지나기 전에 처리할 수 있는지 확인
    if i == 0 : # 조건문 if, else -> i가 0인 경우
        continue # 이번 반복문은 아무것도 실행하지 않음
    else : # i가 0이 아닌 경우
        schedule[i] = True # schedule[i]의 값을 True로 바꿈 -> i일에는 반복문을 돌리고 있는 과제를 해야함
        result += score # result = result + score
print(result) # 출력