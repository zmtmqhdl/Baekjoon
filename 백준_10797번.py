n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
count = 0 # count변수 초기화
for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
    if i == n : # 조건문 if -> i와 n의 같이 같을 경우
        count += 1 # count = count + 1
print(count) # 출력