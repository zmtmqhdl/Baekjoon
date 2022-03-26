t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    n = int(input()) # 값 대입
    data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
    data.sort() # sort를 사용하여 data라는 list의 원소를 오름차순으로 정렬
    result = 0 # 결과값을 저장할 result변수 초기화
    for i in range(2, n) : # 반복문 for -> 2부터 n - 1까지 i에 차례대로 대입하며 반복
        result = max(result, abs(data[i] - data[i - 2])) # 두 통나무 간의 높이의 차 연산
                                                         # 통나무들을 정렬 후 index차이를 2씩 두고 연산
                                                         # 처음 통나무 1 2 3 4 5
                                                         # 정렬 통나무 4 2 1 3 5
    print(result) # 출력