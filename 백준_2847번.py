n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복 
    data.append(int(input())) # append를 사용하여 대입된 값을 data라는 list의 원소로 추가
count = 0 # 결과값을 저장할 count변수 초기화
for i in range(n - 2, -1, -1) : # 반복문 for -> n - 2부터 0까지 -1씩 감소시키며 차례대로 i에 대입하며 반복
    if data[i] >= data[i + 1] : # 조건문 if -> 지급되는 점수가 더 낮은 단계가 높을 경우
        count += data[i] - data[i + 1] + 1 # count = count + data[i] - data[i + 1] + 1
        data[i] = data[i + 1] - 1 # 지급되는 점수를 다음 단계에서 지급되는 점수보다 1점 낮춤
print(count) # 출력