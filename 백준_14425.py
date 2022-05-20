import sys # 라이브러리 호출
n, m = map(int, sys.stdin.readline().split()) # 값 대입
count = 0 # 결과값을 저장할 count변수 초기화
s = set() # s라는 set생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    s.add(str(sys.stdin.readline())) # add를 사용하여 s라는 set에 대입된 값을 원소로 추가
for _ in range(m) : # 반복문 for -> m만큼 반복
    data = sys.stdin.readline() # 값 대입
    if data in s : # 조건문 if -> data의 값이 s라는 set의 원소로 존재하는 경우
        count += 1 # count = count + 1
print(count) # 출력