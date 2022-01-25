n = int(input()) # 값 대입
result = 1 
if n == 0 : # 조건문 if, else
    result = 1
else :
    for i in range(1, n + 1) : # 반복문 for ->  i에 1부터 n까지 차례대로 대입 
        result *= i # result = result * i
print(result) # 출력