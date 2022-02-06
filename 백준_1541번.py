n = list(input().split('-')) # split을 사용하여 대입된 값을 -를 기준으로 나눈 값을 원소로 갖는 n이라는 list생성
sum = 0 # 계산 결과를 저장할 sum변수 초기화
for i in range(0, len(n)) : # 반복문 for -> 0부터 len(n) - 1까지 i에 차례대로 대입하며 반복
    temp = n[i].split('+') # split을 사용하여 n[i]를 +를 기준으로 나눈 값을 temp에 저장
    if i == 0 : # 조건문 if -> 첫 -가 나오기 전까지 모든 값은 덧셈을 함
        for j in temp : # 조건문 if -> temp라는 list의 원소를 차례대로 j에 대입하며 반복
            sum += int(j) # sum = sum + int(j)
    else : # 처음에 대입된 수식을 -를 기준으로 나눠었기 때문에 n[0]을 제외한 모든 수식은 뺄셈을 함 
        for j in temp : # 조건문 if -> temp라는 list의 원소를 차례대로 j에 대입하며 반복
            sum -= int(j) # sum = sum - int(j)
print(sum) # 출력