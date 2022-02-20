data = input() # 값 대입
data = data.replace('XXXX', 'AAAA') # replace를 사용하여 XXXX를 AAAA로 교체
data = data.replace('XX', 'BB') # replace를 사용하여 XX를 BB로 교체
if 'X' in data : # 조건문 if, else -> X가 1개라도 남아있는 경우
    print(-1) # 출력
else : # X가 모두 변환되었을 경우
    print(data) # 출력