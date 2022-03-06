data = input() # 값 대입
ucpc = ['U', 'C', 'P', 'C'] # UCPC문자를 저장하고 있는 ucpc라는 list생성
check = True # UCPC가 만들어지는지 확인하기 위해 True값을 저장하고 있는 check변수 생성
for i in range(len(ucpc)) : # 반복문 for -> 0부터 len(ucpc) - 1까지 i에 차례대로 대입하며 반복
    if ucpc[i] in data : # 조건문 if, else -> ucpc[i]의 값이 data에 존재하는 경우
        idx = data.find(ucpc[i]) # find를 사용하여 data에 ucpc[i]값이 존재하는 index값을 idx변수에 저장 
        data = data[idx + 1:] # data값을 idx + 1번째 index부터 끝까지 새롭게 저장 
    else : # ucpc[i]의 값이 data에 없을 경우
        check = False # UCPC가 만들어지지 않는 것을 확인하기 위해 check변수 False로 저장
        break # 중지
if check == True : # 조건문 if, else -> UCPC가 만들어지는 경우
    print('I love UCPC') # 출력
else : # UCPC가 만들어지지 않는 경우
    print('I hate UCPC') # 출력