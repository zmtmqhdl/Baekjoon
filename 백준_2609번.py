a, b = map(int, input().split()) # 값 대입
def gcd(a, b) : # 함수 생성 -> 최대공약수 구하는 함수
    while b > 0 : # 반복문 while -> b가 0보다 클 경우 반복
        a, b = b, a % b # 유클리드 호제법
    return a # 값 반환
def lcm(a, b) : # 함수 생성 -> 최소공배수 구하는 함수 
    return a * b // gcd(a, b) # 값 반환
print(gcd(a, b)) # 출력
print(lcm(a, b)) # 출력