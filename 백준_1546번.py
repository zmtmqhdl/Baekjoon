n = int(input()) # 값 대입
score = list(map(int, input().split())) # score라는 list에 값 대입
result = 0 # result 초기화
for i in range(n) : # 반복문 for
    result += score[i] / max(score) * 100 # result에 연산 값 합산
print(result / n) # 평균 출력