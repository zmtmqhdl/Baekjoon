def d(n) : # 함수 생성
    n = n + sum(map(int, str(n))) # map(int, str(n)) = [int(n) for i in str(n)]
    return n # 값 반환
NoSelfNumber = set() # NoSelfNumber라는 집합 생성
for i in range(1, 10001) : # 반복문 for
    NoSelfNumber.add(d(i)) # 집합은 중복된 원소를 갖는 것이 불가능
for i in range(1, 10001) : # 반복문 for
    if i not in NoSelfNumber : # 조건문 if
        print(i) # 출력