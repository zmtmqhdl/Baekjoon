s = input() # 값 대입
for i in range(97, 123) : # 반복문 for -> 97부터 122까지 i에 차례대로 대입하며 반복
    result = s.count(chr(i)) # count를 사용하여 chr(i)의 값의 개수를 s라는 값에서 연산 -> chr은 아스키 코드
    print(result, end = ' ') # end를 사용하여 공백을 두고 출력