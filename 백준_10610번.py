n = list((input())) # 대입된 값을 원소로 갖는 n이라는 list생성
n.sort(reverse = True) # sort(reverse = True)를 사용하여 n이라는 list를 내림차순 정렬
sum = 0 # sum변수 초기화
for i in n : # 반목문 for -> n의 원소를 차례대로 i에 대입하며 반복
    sum += int(i) # sum = sum + int(i)
if sum % 3 != 0 or "0" not in n : # 조건문 if, else -> 30의 배수는 일의 자리수가 0이고 각 자리의 숫자들의 더했을 때 3으로 나누어 떨어져야함
    print(-1) # 출력
else :
    print("".join(n)) # join을 사용하여 n이라는 list의 원소를 붙혀서 출력함