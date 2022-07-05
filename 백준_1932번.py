n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(list(map(int, input().split()))) #append를 사용하여 대입된 list를 data라는 list의 원소로 추가
for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 차례대로 i에 대입하며 반복
    for j in range(i + 1) : # 반복문 for -> 0부터 i까지 차레대로 j에 대입하며 반복
        if j == 0 : # 조건문 if, elif, else -> 맨 왼쪽의 수가 선택된 경우
            data[i][j] += data[i - 1][j] # data[i][j] = data[i][j] + data[i - 1][j]
        elif i == j : # 맨 오른쪽의 수가 선택된 경우
            data[i][j] += data[i - 1][j - 1] # data[i][j] = data[i][j] + data[i - 1][j - 1]
        else : # 대각선 왼쪽과 대각선 오른쪽의 수 중에서 큰 값을 연산
            data[i][j] += max(data[i - 1][j], data[i - 1][j - 1]) # data[i][j] = data[i][j] = data[i][j] + max(data[i - 1][j], data[i - 1][j - 1])
print(max(data[n - 1])) # 출력