n = int(input()) # 값 대입
for _ in range(n) : # 반복문 for -> n만큼 반복
    data = list(input()) # data라는 list생성
    sum = 0 # '('가 나오면 1을 더하고 ')'가 나오면 -1을 할 변수sum 초기화
    for i in data : # 반복문 for -> data라는 list의 원소를 차례대로 i에 대입하며 반복
        if i == '(' : # 조건문 if, else -> i가 '('인 경우
            sum += 1 # sum = sum + 1
        else : # i가 ')'인 경우
            sum -= 1 # sum = sum - 1
        if sum == -1 : # 조건문 if -> '('보다 ')'가 이미 더 많이 나온 경우 
            print('NO') # 출력
            break # 중지
    if sum > 0 : # 조건문 if, elif -> '('보다 ')'가 더 많이 나온 경우
        print('NO') # 출력
    elif sum == 0 : # 괄호 문자열이 올바른 괄호 문자열일 경우
        print('YES') # 출력