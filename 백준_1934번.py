t = int(input()) # 값 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    a, b = map(int, input().split()) # 값 대입
    aa, bb = a, b # aa, bb변수에 a, b변수의 값을 각각 저장
    while bb != 0 : # 반복문 while -> bb가 0이 아닐 경우 반복
        aa = aa % bb # aa변수에 aa % bb의 값을 저장
        aa, bb = bb, aa # aa, bb변수에 bb, aa변수의 값을 각각 저장
    print(a * b // aa) # 출력