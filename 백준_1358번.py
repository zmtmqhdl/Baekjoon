import sys # 라이브러리 호출
input = sys.stdin.readline # input에 sys.stdin.readline을 저장하여 값 대입을 빠르게 처리
W, H, X, Y, P = map(int, input().split()) # 값 대입
count = 0 # 결과값을 저장할 count변수 초기화
for _ in range(P) : # 반복문 for -> P만큼 반복
    x, y = map(int, input().split()) # 값 대입
    if (X <= x <= X + W) and (Y <= y <= Y + H) : # 조건문 if -> 선수가 직사각형 안에 있는 경우
        count +=1 # count = count + 1
        continue # 이번 반복을 종료하고 다음 반복 실행
    r = H / 2 # 반지름 연산
    d1 = ((x - X) ** 2 + (y - (Y + r)) ** 2) ** 0.5 # 왼쪽 반원 연산
    d2 = ((x- (X + W)) ** 2 + (y - (Y + r)) ** 2) ** 0.5 # 오른쪽 반원 연산
    if d1 <= r or d2 <= r : # 조건문 if -> 선수가 반원 안에 있는 경우
        count += 1 # count = count + 1
print(count) # 출력