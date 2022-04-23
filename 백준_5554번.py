a = 0 # 결과값을 저장할 변수a 초기화
for i in range(1, 5) : # 반복문 for -> 1부터 4까지 i에 차례대로 대입하며 반복
    a += int(input()) # a = a + int(input())
print(a // 60) # 분 출력
print(a % 60) # 초 출력