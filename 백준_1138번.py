n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
line = [0] * n # 줄의 정보를 저장할 [0] * n형태의 line이라는 list생성
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    count = 0 # line이라는 list에서 선택된 위치가 몇 번째 index인지 알기 위한 count변수 초기화
    for j in range(n) : # 반복문 for -> 0부터 n - 1까지 차례대로 j에 대입하며 반복
        if count == data[i] and line[j] == 0 : # 가정문 if, elif -> 왼쪽에 사람이 있는 수가 같으면서 자리가 비어있는 경우
            line[j] = i + 1 # 자리에 사람을 배치
            break # 중지
        elif line[j] == 0 : # 자리가 비어있지 않은 경우
            count += 1 # count = count + 1
print(' '.join(map(str, line))) # 출력