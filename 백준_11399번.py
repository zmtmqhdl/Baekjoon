n = int(input()) # 테스트 횟수 대입
time_data = list(map(int, input().split())) # 입력된 값들을 원소로 갖는 time_data라는 list생성
time_data.sort() # sort를 사용하여 time_data를 오름차순으로 정렬
sum = 0 # 필요한 시간의 합의 최솟값을 저장할 sum변수 초기화
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    for j in range(i + 1) : # 반목문 for -> 0부터 i까지 j에 차례대로 대입하며 반복
        sum += time_data[j] # sum = sum + time_data[j]
print(sum) # 출력