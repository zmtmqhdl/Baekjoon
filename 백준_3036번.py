import fractions # 라이브러리 호출
n = int(input()) # 값 대입
data = list(map(int, input().split())) # 대입된 값을 원소로 갖는 data라는 list생성
for i in range(1, n) : # 반복문 for -> 1부터 n -1까지 i에 차례대로 대입하며 반복
    a = fractions.Fraction(data[i], data[0]) # fractions.Fraction(분자, 분모)을 사용하여 기약분수 연산
    print(str(a.denominator) + '/' + str(a.numerator)) # denominator를 사용하여 분모, numerator를 사용하여 분자를 찾아내 출력