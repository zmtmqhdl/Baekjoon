import sys # 라이브러리 호출
n, k = map(int,sys.stdin.readline().split()) # 값 대입
data = list(map(int,sys.stdin.readline().rstrip())) # 대입된 값을 원소로 갖는 data라는 list생성
result = [] # result라는 list생성
count = k # 숫자를 제거한 횟수를 저장할 count라는 변수에 k값 저장
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 차례대로 i에 대입하며 반복
    while count > 0 and result : # 반복문 while -> count가 0보다 크고 result가 True일 경우 반복
        if result[len(result) - 1] < data[i] : # 조건문 if -> result의 마지막 원소가 data[i]보다 작을 경우
            result.pop() # pop을 사용하여 result라는 list의 가장 마지막 원소 삭제
            count -= 1 # count = count - 1
        else : # result의 마지막 원소가 data[i]보다 큰 경우
            break # 중지
    result.append(data[i]) # append를 사용하여 data[i]를 result라는 list의 원소로 대입
for i in range(n - k) : # 반복문 for -> 0부터 n - k - 1까지 차례대로 i에 대입하며 반복
    print(result[i], end = "") # 출력