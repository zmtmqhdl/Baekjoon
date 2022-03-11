data = [] # data라는 list생성
for _ in range(5) : # 반복문 for -> 5회 반복
    data.append(int(input())) # append를 사용하여 대입된 값을 data의 원소로 대입
print(min(data[0], data[1], data[2]) + min(data[3], data[4]) - 50) # min을 사용하여 최솟값 출력