import sys # 라이브러리 호출
t = int(sys.stdin.readline()) # 테스트 횟수 대입 -> sys.stdin.readline() = input()
for _ in range(t) : # 반복문 for -> t만큼 반복
    n = int(sys.stdin.readline()) # 값 대입
    data = [] # data라는 list생성
    count = 1 # 치용 할 수 있는 신입 사원의 수를 저장할 count변수 생성
    for _ in range(n) : # 반복문 for -> n만큼 반복
        x, y = map(int, sys.stdin.readline().rstrip().split()) # 값 대입
        data.append([x, y]) # append를 사용하여 [x, y]를 data라는 list에 원소로 추가
    data.sort() # sort를 사용하여 data라는 list를 오름차순으로 정렬
    check = data[0][1] # 면접 성적을 비교하기 위한 check변수를 생성하고 서류 성적이 1등인 사원의 면접 성적을 저장
    for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 i에 차레대로 대입하며 반복
        if check > data[i][1] : # 조건문 if -> 면접 성적 비교
            count += 1 # count = count + 1
            check = data[i][1] # 비교 대상을 data[i][1]로 교체
    print(count) # 출력