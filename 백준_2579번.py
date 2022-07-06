n = int(input()) # 값 대입
score = [0] * 301 # 0을 원소로 301개 갖는 score라는 list생성
data = [0] * 301 # 0을 원소로 301개 갖는 data라는 list생성
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 차례대로 i에 대입하며 반복
    score[i] = int(input()) # 값 대입
data[1] = score[1] # data[1]에 score[1]저장
data[2] = score[1] + score[2] # data[2]에 score[1] + score[2]저장
for i in range(3, n + 1) : # 반복문 for -> 3부터 n까지 차례대로 i에 대입하며 반복
    data[i] = max(data[i - 3] + score[i - 1] + score[i], data[i - 2] + score[i]) # max를 사용하여 data[i - 3] + score[i - 1] + score[i], data[i - 2] + score[i] 중 더 큰 값을 data[i]에 저장
print(data[i]) # 출력