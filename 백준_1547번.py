n = int(input()) # 값 대입
cup = [1, 2, 3] # 공의 위치를 저장할 cup이라는 list생성
for _ in range(n) : # 반복문 for -> n만큼 반복
    x, y = map(int, input().split()) # 값 대입
    xi = cup.index(x) # 컵의 위치 index값을 xi라는 변수에 저장
    yi = cup.index(y) # 컵의 위치 index값을 yi라는 변수에 저장
    cup[xi], cup[yi] = cup[yi], cup[xi] # 컵끼리의 위치 변환
print(cup[0]) # 출력