t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    a, b = map(int, input().split(',')) # split(',')을 사용하여 ,을 기준으로 대입된 값을 나눠 a, b에 대입
    print(a + b) # 출력