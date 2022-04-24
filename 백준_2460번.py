passenger = 0 # 현재 탑승 중인 승객의 수를 저장할 passenger변수 초기화
max_passenger = 0 # 기차에 탑승했던 최대인원의 수를 저장할 max_passenger변수 초기화
for _ in range(10) :
    out_train, in_train  = map(int, input().split()) # 값 대입
    passenger += in_train - out_train # passenger = passenger + in_train - out_train
    max_passenger = max(passenger, max_passenger) # max를 사용하여 passenger, max_passenger 중 큰 값을 max_passenger로 설정
print(max_passenger) # 출력