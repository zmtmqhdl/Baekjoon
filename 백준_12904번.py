s = list(map(str, input())) # 대입된 값을 원소로 가지는 s라는 list생성
t = list(map(str, input())) # 대입된 값을 원소로 가지는 t라는 list생성
while len(s) != len(t): # 반복문 while -> len을 사용하여 s의 길이와 t의 길이가 같지 않을 동안 반복
    if t[-1] == 'A' : # 조건문 if, elif -> t의 마지막 문자가 'A'일 경우
        t.pop() # pop을 사용하여 t의 마지막 문자 제거
    elif t[-1] == 'B' : # t의 마지막 문자가 'B'일 경우
        t.pop() # pop을 사용하여 t의 마지막 문자 제거
        t = t[::-1] # t
if s == t : # 조건문 if, else -> s와 t가 같을 경우
    print(1) # 출력
else : # s와 t가 다를 경우
    print(0) # 출력
