n, m = map(int, input().split()) # 값 대입
card = list(map(int, input().split())) # 입력된 값을 갖는 card라는 list생성
sum = 0 # 선택된 3장의 카드의 합을 저장할 sum이라는 변수 생성
for a in card : # 반복문 for -> card의 원소를 차례대로 a에 대입
    for b in card : # 반복문 for -> card의 원소를 차례대로 b에 대입
        for c in card : # 반복문 for -> card의 원소를 차례대로 c에 대입
            if a != b and b != c and a != c and a + b + c > sum and a + b + c <= m : # 조건문 if -> a, b, c가 서로 값이 다르고 a, b, c의 합이 기존의 sum보다 크고 m보다 작거나 같다면
                sum = a + b + c # sum을 새로운 a + b + c로 지정
print(sum) # 출력