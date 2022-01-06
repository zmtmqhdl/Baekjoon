a = int(input()) # input을 사용하여 a에 값 대입, 바로 계산에 사용하므로 int형으로 대입
b = input() # 자릿수를 나눠서 곱해야하므로 str형으로 b에 값 대입
print(a * int(b[2])) # b의 3번째 글자를 int형으로 변환하여 계산
print(a * int(b[1])) # b의 2번째 글자를 int형으로 변환하여 계산
print(a * int(b[0])) # b의 1번째 글자를 int형으로 변환하여 계산
print(a * int(b)) # b를 int형으로 변환하여 계산