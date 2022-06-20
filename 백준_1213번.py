n = list(map(str, input())) # 값 대입
answer = '' # 변수 초기화
temp = '' # 변수 초기화
odd = 0 # 홀수인 문자의 개수를 확인할 odd변수 초기화
count = [0 for _ in range(26)] # 0을 25개를 원소로 갖는 count라는 list생성
for i in n : # 반복문 for -> 0부터 n - 1까지 i에 차례대로 대입하며 반복
    count[ord(i) - 65] += 1 # count[ord(i) - 65] = count[ord(i) - 65] + 1 
for i in range(26) : # 반복문 for -> 0부터 25까지 i에 차례대로 대입하며 반복
    if count[i] % 2 == 1: # 조건문 if -> 문자가 홀수인 경우
        odd += 1 # odd = odd + 1
        temp = chr(i + 65) # 홀수인 문자를 temp라는 변수에 저장
    answer += chr(i + 65) * (count[i] // 2) # 짝수개인 문자를 절반만 입력
reverse_answer = list(answer) # answer를 원소로 갖는 reverse_answer라는 list생성
reverse_answer.reverse() # reverse를 사용하여 원소를 뒤집음
if odd > 1 : # 조건문 if -> 개수가 홀수인 문자가 2개 이상인 경우
    print("I'm Sorry Hansoo") # 출력
else : # 개수가 홀수인 문자가 1개인 경우
    print(answer + temp + ''.join(map(str, reverse_answer))) # 출력