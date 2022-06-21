import sys # 라이브러리 호출
n, m = map(int, sys.stdin.readline().split()) # 값 대입
dict = {} # dict이라는 dictionary생성
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 i에 차례대로 대입하며 반복
    a = sys.stdin.readline().rstrip() # 값 대입
    dict[i] = a # dict라는 dictionary에 원소 대입
    dict[a] = i # dict라는 dictionary에 원소 대입
for i in range(m) : # 반복문 for -> 0부터 m - 1까지 i에 차례대로 대입하며 반복
    quest = sys.stdin.readline().rstrip() # 값 대입
    if quest.isdigit() : # 조건문 if -> quest가 숫자인 경우
        print(dict[int(quest)]) # 출력
    else : # quest가 문자인 경우
        print(dict[quest]) # 출력