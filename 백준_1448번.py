import sys # 라이브러리 호출
n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(sys.stdin.readline())) # append를 사용하여 대입된 값을 data라는 list의 원소로 대입
data.sort(reverse = True) # sort(reverse = True)를 사용하여 data라는 list의 원소를 내림차순으로 정렬
istrue = False # 삼각형을 만들 수 있는지 확인하기 위한 istrue변수에 False값 저장
for i in range(len(data) - 2) : # 반복문 for -> 0부터 len(data) - 3까지 i에 차례대로 대입하며 반복
    if data[i] < data[i + 1] + data[i + 2] : # 조건문 if -> 삼각형을 만들 수 있는 경우
        print(data[i] + data[i + 1] + data[i + 2]) # 출력
        istrue = True # 삼각형을 만들 수 있으므로 istrue변수에 True값 저장
        break # 중지
if istrue == False : # 조건문 if -> 삼각형을 만들 수 없는 경우
    print(-1) # 출력