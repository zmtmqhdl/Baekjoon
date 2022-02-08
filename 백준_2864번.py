a, b= input().split() # 값 대입
min = int(a.replace('6', '5')) + int(b.replace('6', '5')) # replace를 사용하여 6을 5로 바꿔서 a와 b를 더한 값을 min변수에 저장
max = int(a.replace('5', '6')) + int(b.replace('5', '6')) # replace를 사용하여 5를 6으로 바꿔서 a와 b를 더한 값을 max변수에 저장
print(min, max) # 출력