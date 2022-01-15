n = int(input()) # 값 대입
if n < 100 : # 조건문 if, else -> 100미만의 수는 모두 등차수열
    print(n) # 출력
else :
    result = 99 # n이 100이상이면 99까지는 모두 등차수열 이므로 result 값을 99로 초기화
    for i in range(100, n + 1) : # 반복문 for
        data = list(map(int, str(i))) # list(map(int, str(i))) -> i의 값을 str형으로 바꾸어 한 문자씩 int형으로 다시 바꿔 list에 넣음
        if data[0] - data[1] == data[1] - data[2] : # 조건문 if -> 각 자릿수의 차이 연산
            result += 1 # result = result + 1
    print(result) # 출력