data = [0, 1] # 피보나치 수열을 저장할 data라는 list생성
n = int(input()) # 값 대입
i = 2 # 피보나치 수열의 연산에 필요한 i변수 생성 후 2를 저장
while n + 1 != len(data) : # 반복문 while -> 대입된 값에 1을 더한 값과 len(data)의 값이 같지 않을 경우 반복
    data.append(data[i - 2] + data[i - 1]) # append를 사용하여 연산된 값을 data라는 list의 원소에 대입
    i += 1 # i = i + 1
print(data[n]) # 출력