n = int(input()) # 값 대입
def a(n) : # 함수 생성
    if n <= 1 : # 가정문 if, else -> n이 1이하일 때는 반환값이 n과 같음
        return n # n을 반환
    else : 
        return a(n - 1) + a(n - 2) # 피보나치 수 구현
print(a(n)) # 출력