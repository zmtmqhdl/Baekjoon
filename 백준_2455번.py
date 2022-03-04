data = [] # data라는 list생성
for _ in range(4) : # 반복문 for -> 4회 반복
    x, y = map(int, input().split()) # 값 대입
    data.append([x, y]) # append를 사용하여 [x, y]의 값을 data라는 list에 2중 배열형태로 대입
max = 0 # 결과값을 저장할 cnt라는 변수 초기화
human = 0 # 사람의 수를 저장할 human이라는 변수 초기화
for i in range(4) : # 반복문 for -> 0부터 3까지 i에 차례대로 대입하며 반복
    human += data[i][1] # human = human + data[i][0] -> 기차에 탄 사람
    human -= data[i][0] # human = human - data[i][1] -> 기차에서 내린 사람
    if human > max : # 조건문 if -> 현재 기차에 탄 사람이 기존에 기차에 탔던 사람 수보다 많을 경우
        max = human # max값을 human으로 변경
print(max) # 출력