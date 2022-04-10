n = int(input()) # 값 대입
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 i에 차례대로 대입하며 반복
    result = ' ' * (n - i) + '*' * ((2 * i) - 1) # 연산
    print(result) # 출력