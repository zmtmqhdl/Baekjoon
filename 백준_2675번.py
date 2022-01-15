t = int(input()) # 테스트 횟수 대입
for _ in range(t) : # 반복문 for
    r, s = input().split() # 값 대입
    for i in range(len(s)) : # 반복문 for -> s의 길이만큼 반복
        temp = s[i] * int(r) # s의 문자를 순서대로 r번 반복 -> input을 하게 되면 str형으로 값을 저장하므로 r을 int형을 변환시켜 연산
        if i != (len(s) - 1) : # 조건문 if
            print(temp, end = '') # # end = ' '를 사용하여 print후 개행이 아닌 띄어쓰기를 하도록 하여 출력
        else :
            print(temp) # 출력