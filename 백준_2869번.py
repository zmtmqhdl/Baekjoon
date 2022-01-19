import sys # sys라이브러리 호출
a, b, v = map(int, sys.stdin.readline().split()) # 값 대입 -> sys.stdin.readline()은 input()과 같지만 속도가 더 빠름
result = (v - b) / (a - b) # a - b로만 나누게 되면 정상에 올라간 후 미끄러지는 것도 포함하게 되므로 v - b를 a - b로 나누어야 함
if result == int(result) : # 조건문 if -> 만약  result가 int(result)와 같다면 
                           # 정수
    print(int(result)) # result를 int형으로 변환하여 출력
else : # result가 int형이 아니라면
       # 정수가 아님
    print(int(result) + 1) # result를 int형으로 변환하고 소수점도 하루로 계산해야하므로 int(result) + 1로 계산하여 출력