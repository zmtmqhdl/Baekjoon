n = int(input()) # 값 대입
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 i에 차례대로 대입하며 반복
    print("*" * i + " " * 2*(n-i) + "*" * i) # 출력
for j in range(1, n) : # 반복문 for -> 1부터 n - 1까지 i에 차례대로 대입하며 반복
    print("*" * (n - j) + " " * 2 * j + "*" * (n - j)) # 출력