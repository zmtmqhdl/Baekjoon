import sys # 라이브러리 호출
n = int(sys.stdin.readline()) # 값 대입
n_data = set(map(int, sys.stdin.readline().split())) # 대입된 값을 원소로 갖는 n_data라는 set생성
m = int(sys.stdin.readline()) # 값 대입
m_data = list(map(int, sys.stdin.readline().split())) # 대입된 값을 원소로 갖는 m_data라는 list생성
for i in m_data : # 반복문 for -> m_data라는 list의 원소를 차례대로 i에 대입하며 반복
    if i in n_data : # 조건문 if, else -> i가 n_data라는 set에 원소로 존재하는 경우
        print(1) # 출력
    else : # i가 n_data라는 set에 원소로 존재하지 않는 경우
        print(0) # 출력