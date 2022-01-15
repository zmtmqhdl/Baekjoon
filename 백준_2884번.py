a, b = map(int, input().split()) # 값 대입
if b - 45 < 0 : # 조건문 if, else
    b += 15 # b = b + 15
    a -= 1 # a = a - 1
    if a < 0 : # 조건문 if
        a = 23
else :
    b -= 45
print(a, b) # 출력
