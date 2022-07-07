import sys # 라이브러리 호출
input = sys.stdin.readline # input변수에 sys.stdin.readline저장
data = [] # data라는 list생성
n = int(input()) # 값 대입
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(list(map(int, input().split()))) # append를 사용하여 입력된 list를 data라는 list의 원소로 추가
for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 차례대로 i에 대입하며 반복
    data[i][0] += min(data[i - 1][1], data[i - 1][2]) # data[i][0] = min(data[i - 1][1], data[i - 1][2]) + data[i][0]
    data[i][1] += min(data[i - 1][0], data[i - 1][2]) # data[i][1] = min(data[i - 1][0], data[i - 1][2]) + data[i][1]
    data[i][2] += min(data[i - 1][0], data[i - 1][1]) # data[i][2] = min(data[i - 1][0], data[i - 1][1]) + data[i][2]
print(min(data[-1])) # min을 사용하여 data라는 list의 마지막 원소 중 최소값을 출력