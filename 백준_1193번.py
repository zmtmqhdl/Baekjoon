x = int(input()) # 값 대입
line = 0 # 몇 번째 대각선에 있는지 확인하기 위한 변수
while x > line : # 반복문 while -> x가 line보다 클 동안 반복
    x -= line # x = x - 1 -> x가 몇 번째 대각선에 있는지 연산하는 과정
    line += 1 # line = line + 1 -> x가 몇 번째 대각선에 있는지 연산하는 과정
if line % 2 == 0 : # 가정문 if, else -> line이 짝수일 때
    a = x # 분자 오름차순
    b = line - x + 1 # 분모 내림차순
else : # line이 홀수일 때
    a = line - x + 1 # 분자 내림차순
    b = x # 분모 오름차순
print(a, '/', b, sep = '') # sep를 사용해 띄어쓰기 없이 출력