n = int(input()) # 값 대입
member = input() # 값 대입
count = member.count('LL') # count를 사용하여 member라는 변수에 LL문자가 몇 개 있는지 확인
if (count <= 1) : # 조건문 if, else -> 커플석이 1개 이하일 경우
    print(len(member)) # len을 사용하여 member변수의 길이 출력
else : # 커플석이 2개 이상일 경우
    print(len(member) - count + 1) # 출력ㅌ