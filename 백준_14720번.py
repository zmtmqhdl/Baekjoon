n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
count = 0 # 결과값을 저장할 count변수 초기화
milk = 0 # 우유의 종류를 저장할 milk변수 초기화
for i in data : # 반복문 for -> data의 원소를 차례대로 i에 대입하며 반복
    if i == milk : # 조건문 if -> i와 milk가 일치할 경우
        count += 1 # count = count + 1
        milk += 1 # milk = milk + 1
        if milk == 3 : # 조건문 if -> 바나나 우유를 마셨을 경우
            milk = 0 # 딸기 우유를 마셔야 하는 경우로 변경
print(count) # 출력