n = int(input()) # 값 대입
road_data = list(map(int, input().split())) # 값 대입
cost_data = list(map(int, input().split())) # 값 대입
min_price = cost_data[0] # 주유소의 최솟값을 저장할 min_pirce변수 생성 후 cost_data[0]의 값 저장
sum = 0 # 비용의 합을 저장할 sum변수 초기화
for i in range(len(road_data)) : # 반복문 for -> 0부터 len(road_data) - 1까지 i에 차례대로 대입하며 반복
    if cost_data[i] >= min_price : # 조건문 if, elif -> 다음 도시의 주유소 가격보다 현재 머문 주유소의 가격이 더 저렴한 경우
        sum += min_price * road_data[i] # sum = sum + (min_price * road_data[i])
    elif cost_data[i] < min_price : # 다음 도시의 주유소 가격이 현재 머문 주유소의 가격보다 저렴한 경우
        min_price = cost_data[i] # 주유소의 최솟값 변경
        sum += min_price * road_data[i] # sum = sum + (min_price * road_data[i])
print(sum) # 출력