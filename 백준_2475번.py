data = list(map(int, input().split())) # 대입된 값을 원소로 가지는 data라는 list생성
result = 0 # 결과값을 저장할 result변수 초기화
for i in data : # 반복문 for -> data의 원소를 i에 차례대로 대입하며 반복
    result += i ** 2 # result = result + i ** 2
print(result % 10) # 출력