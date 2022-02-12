a = str(input()) # 값 대입
b = str(input()) # 값 대입
count = 0 # 결과값을 저장할 count변수 초기화
n = 0 # index값을 저장할 n변수 초기화
while n <= len(a) - len(b) : # 반복문 while
    if a[n:n + len(b)] == b : # 조건문 if, else -> n번째 문자부터 n + len(b)까지의 문자가 b와 같을 경우
        count += 1 # count = count + 1
        n += len(b) # n = n + len(b)
    else :
        n += 1 # n = n + 1 -> 다음 index부터 다시 조사
print(count) # 출력