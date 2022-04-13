n = int(input()) # 값 대입
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 차례대로 i에 대입하며 반복
    print(' ' * (n - i) + '*' * i) # 출력
for i in range(1, n) : # 반복문 for -> 1ㅜ터 n - 1까지 차례대로 i에 대입하며 반복
    print(' ' * i + '*' * (n - i)) # 출력