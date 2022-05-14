n = int(input()) # 값 대입
n_data = set(map(int, input().split())) # 대입된 값을 원소로 갖는 n_data라는 set생성
m = int(input()) # 값 대입
m_data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 m_data라는 list생성
for i in m_data : # 반복문 for -> m_data라는 list의 원소를 i에 차례대로 대입하며 반복
    if i in n_data : # 조건문 if, else -> i가 n_data라는 set의 원소에 포함된 경우
        print(1, end = ' ') # 출력
    else : # i가 n_data라는 set의 원소에 포함되지 않은 경우
        print(0, end = ' ') # 출력