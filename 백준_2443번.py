a = int(input()) # 값 대입
b = a # b라는 변수에 a대입
for i in range(1, a + 1) : # 반복문 for -> 1부터 a까지 i에 차례대로 대입하며 반복
    print(' ' * (b - i) + '*' * (2 * i - 1)) # 출력
for j in range(1, a) : # 반복문 for -> 1부터 a - 1까지 i에 차례대로 대입하며 반복
    print(' ' * j + '*' * (2 * (b - j) - 1)) # 출력