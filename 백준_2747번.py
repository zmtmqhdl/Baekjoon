data = [0, 1] # 피나치 수를 저장할 data라는 list생성
while len(data) <= 45 : # 반복문 while -> len(data)의 값이 45이하일 경우 반복
    data.append(data[-2] + data[-1]) # append를 사용하여 연산한 피보나치 수를 대입
n = int(input()) # 값 대입
print(data[n]) # 출력