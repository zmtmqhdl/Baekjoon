import sys # 라이브러리 호출
a, b = map(int, sys.stdin.readline().split()) # 값 대입 -> sys.stdin.readline() = input()
count = 1 # a를 b로 바꾸는데 필요한 연산의 횟수를 구하기 위한 count변수 생성 -> a를 b로 바꾸는데 필요한 연산의 최솟값에 1을 더해서 출력함
while a != b : # 반복문 while -> a와 b의 값이 다를 경우 반복
    count += 1 # count = count + 1
    temp = b # b로 a를 만들 수 없는 경우를 확인하기 위한 temp변수 생성
    if b % 10 == 1 : # 조건문 if -> b의 마지막 자리의 문자가 1일 경우
        b //= 10 # b = b // 10
    elif b % 2 == 0 : # 조건문 if -> b의 마지막 자리의 문자가 0 또는 2일 경우
        b //= 2 # b = b // 2
    if b == temp : # 조건문 if -> b가 제시된 연산이 불가능할 경우 b == temp가 성립
        count = -1
        break # 중지
print(count) # 출력