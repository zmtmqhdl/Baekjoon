t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for -> t만큼 반복
    k = int(input()) # 값 대입
    n = int(input()) # 값 대입
    people = [i for i in range(1, n + 1)] # 1 ~ n까지의 원소를 갖는 people이라는 list 생성
    for _ in range(k) : # 반복문 for -> k만큼 반복
        for i in range(1, n) : # 반복문 for -> i는 index로 활용됨
            people[i] += people[i - 1] # people[i] = people[i] + people[i - 1]
                                       # 아래층과 왼쪽층의 사람 수의 합
    print(people[-1]) # 슬라이싱을 이용하여 people이라는 list에서 가장 마지막 원소 출력