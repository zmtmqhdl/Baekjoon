import sys # 라이브러리 호출
t = int(input()) # 테스트 횟수 대입
for i in range(t) : # 반복문 for -> t만큼 반복
    a, b = map(int, sys.stdin.readline().rstrip().split()) # sys.stdin.readline().rstrip()은 input()에 비해서 처리속도가 빠름
    print(a + b) # 출력