n = int(input()) # 값 대입
card = list(map(int, input().split())) # 대입된 값을 원소로 갖는 card라는 list생성
m = int(input()) # 값 대입
quest = list(map(int, input().split())) # 대입된 값을 원소로 갖는 quest라는 list생성
dict = {} # dict라는 집합 생성
for i in card : # 반복문 for -> card라는 list의 원소를 차례대로 i에 대입하며 반복
    if i in dict : # 조건문 if -> i가 dict라는 집합의 원소로 존재하는 경우
        dict[i] += 1 # dict[i] = dict[i] + 1
    else : # i가 dict라는 집합의 원소로 존재하지 않는 경우
        dict[i] = 1 # dict[i]의 값을 1로 변경
for i in quest : # 조건문 if -> quest라는 list의 원소를 차례대로 i에 대입하며 반복
    if i in dict : # 조건문 if -> i가 dict라는 집합의 원소로 존재하는 경우
        print(dict[i], end = ' ') # 출력
    else : # i가 dict라는 집합의 원소로 존재하지 않는 경우
        print(0, end = ' ') # 출력