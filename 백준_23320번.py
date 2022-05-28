n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
x, y = map(int, input().split()) # 값 대입
result = [] # 절대평가 시 A학점을 받을 수 있는 학생들을 모을 result라는 list새엇ㅇ
for i in data : # 반복문 data -> data의 원소를 차례대로 i에 대입하며 반복
    if int(i) >= y : # 조건문 if -> 상대평가 시 int(i)가 y점수 이상일 경우
        result.append(int(i)) # append를 사용하여 int(i)를 result라는 list의 원소로 추가
print(round((n * (x / 100))), len(result), sep = ' ') # 출력