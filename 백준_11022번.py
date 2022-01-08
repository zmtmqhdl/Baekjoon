t = int(input()) # 테스트 횟수 대입
for i in range(t) : # 반복문 for -> t만큼 반복
    a, b = map(int, input().split()) # 값 대입
    print("Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(a + b)) # int형을 str형으로 변환시켜 +를 사용해 출력할 수 있음