n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
result = 0 # 결과값을 저장할 result변수 초기화
score = 0 # 연속된 점수를 계산할 score변수 초기화
for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
    if i == 1 : # 조건문 if , else -> 답이 맞은 경우
        score += 1 # scroe = score + 1
        result += score # result = result + score
    else : # 답이 틀린 경우
        score = 0 # 연속된 점수 초기화
print(result) # 출력