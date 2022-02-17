n = int(input()) # 값 대입
blank = 0 # 공백을 나타내기 위한 blank변수 초기화
while n != 0 : # 반복문 while -> n이 0이 아닐 경우 반복
    print(' ' * blank + '*' * n) # 출력
    n -= 1 # n = n - 1
    blank += 1 # blank = blank + 1