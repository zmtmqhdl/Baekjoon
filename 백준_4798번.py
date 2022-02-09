i = 1 # 케이스의 수를 셀 i변수 생성
while True : # 반복문 while -> False가 나올 때까지 반복
    l, p, v = map(int, input().split()) # 값 대입
    if l == p == v == 0 : # 조건문 if -> l, p, v의 값이 0일 경우
        break # 중지
    count = (v // p) * l # p일 중 l일동안 사용할 수 있는 총일자 계산
    count += min((v % p), l) # count = count + min((v % p), l)
    print(f'Case {i}: {count}') # fstring을 사용하여 출력
    i += 1 # i = i + 1 -> 케이스 수 증ㄱ아