def d(n) : # 함수 생성
    n = n + sum(list(map(int, str(n)))) # list(map(int, str(n))) -> n의 값을 str형으로 바꾸어 한 문자씩 int형으로 다시 바꿔 list에 넣음
    return n # 값 반환
NoSelfNumber = set() # NoSelfNumber라는 집합 생성
for i in range(1, 10001) : # 반복문 for
    NoSelfNumber.add(d(i)) # 집합은 중복된 원소를 갖는 것이 불가능
for i in range(1, 10001) : # 반복문 for
    if i not in NoSelfNumber : # 조건문 if
        print(i) # 출력
