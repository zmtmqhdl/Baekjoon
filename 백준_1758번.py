n = int(input()) # 값 대입
data = [] # data라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    data.append(int(input())) # append를 사용하여 대입된 값을 data라는 list의 원소로 대입
data.sort(reverse = True) # sort(reverse = True)를 사용하여 data의 원소를 내림차순으로 정렬
rank = 1 # 순위를 저장할 rank변수 1로 초기화
result = 0 # 결과를 저장할 result변수 초기화
for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
    money = i - (rank - 1) # 팁 연산
    if money > 0 : # 조건문 if -> 팁이 1이상일 경우
        result += money # result = result + money
    rank += 1 # rank = rank + 1
print(result) # 출력