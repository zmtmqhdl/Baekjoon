n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
young_min = data[n] # 에너지가 가장 낮은 크루의 에너지
young_max = data[2 * n - 1] # 에너지가 가장 큰 크루의 에너지
print(young_max - young_min) # 출력