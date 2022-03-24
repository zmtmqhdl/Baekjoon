import sys # 라이브러리 호출
n = int(sys.stdin.readline()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(sys.stdin.readline())) # append를 사용하여 대입된 값을 data라는 list의 원소로 대입
data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
result = 0 # 결과값을 저장할 result변수 초기화
for i in range(n) : # 반복문 for -> n만큼 반복
    result += abs(data[i] - (i + 1)) # result = result + abs(data[i] - (i + 1))
                                     # abs를 사용하여 절댓값을 연산
print(result) # 출력