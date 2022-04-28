n = int(input()) # 값 대입
for i in range(n) : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    a, b = map(int, input().split()) # 값 대입
    print("Case " + str(i + 1) + ":", a + b) # 출력