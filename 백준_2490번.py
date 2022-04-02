for _ in range(3): # 반복문 for -> 3번 반복
    a = list(map(int, input().split())) # 대입된 값을 원소로 갖는 a라는 list생성
    if a.count(0) == 1 : # 조건문 if, elif, else -> count를 사용하여 0의 개수 파악
                         # 도
        print("A") # 출력
    elif a.count(0) == 2 : # 개
        print("B") # 출력
    elif a.count(0) == 3 : # 걸
        print("C") # 출력
    elif a.count(0) == 4 : # 윷
        print("D") # 출력
    else : # 모
        print("E") # 출력