n = int(input()) # 값 대입
count = 2 # 처음 나누는 값을 2로 지정하기 위함
while n != 1 : # 반복문 while -> n이 1이 아닌 경우 반복
    if n % count == 0 : # 조건문 if, else -> n이 count로 나눠떨어진다면
        n //= count # n = n // count 
        print(count) # 출력
    else :
        count += 1 # count = count + 1