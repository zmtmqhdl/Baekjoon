chess = [] # chess라는 list생성
for _ in range(8) : # 반복문 for -> 8만큼 반복
    chess.append(list(map(str, list(input())))) # append를 사용하여 대입된 값을 chess라는 list의 원소로 대입
answer = 0 # 결과값을 저장할 answer변수 초기화
for i in range(8) : # 반복문 for -> 0부터 7까지 차례대로 i에 대입하며 반복
    for j in range(8) : # 반복문 for -> 0부터 7까지 차례대로 j에 대입하며 반복
        if (i + j) % 2 == 0 : # 조건문 if -> 하얀 칸일 경우
            if chess[i][j] == 'F' : # 말이 있을 경우
                answer += 1 # answer = answer + 1
print(answer) # 출력