n = int(input()) # 값 대입
for i in range(1, n + 1) : # 반복문 for -> 1부터 n까지 i에 차례대로 대입하며 반복
    print("*" * i) # 출력
for i in range(n - 1, 0, -1) : # 반복문 for -> n - 1부터 1까지 -1씩 감소시키며 i에 차례대로 대입하며 반복 
    print("*" * i) # 출력