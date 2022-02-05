n = int(input()) # 값 대입
def move(n, a, b, c) : # m함수 선언
                       # n은 옮겨야하는 수, a는 1번탑, b는 2번탑, c는 3번탑
    if n == 1 : # 조건문 if -> 장판이 1개인 경우는 바로 1번탑에서 3번탑으로 이동
        print(a, c) # 출력
    else :
        move(n - 1, a, c, b) # move함수 실행
        print(a, c) # 출력
        move(n - 1, b, a, c) # move함수 실행
print(2 ** n - 1) # 출력
move(n, 1, 2, 3) # 함수 실행