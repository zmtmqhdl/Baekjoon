t = int(input()) # 테스트 횟수 대입
for i in range(t): # 반복문 for
    h, w, n = map(int, input().split()) # 값 대입
    floor = n % h # 몇 층인지 구하는 연산
    room = n // h + 1 # 몇 호실인지 구하는 연산
    if floor == 0: # 조건문 if -> 건물 층수의 배수인 경우
        room -= 1 # room = room - 1
        floor = h
    print(floor*100 + room) # 출력