x = int(input()) # 값 대입
y = int(input()) 
if x > 0 and y > 0 : # 조건문 if, elif, else
    print("1")
elif x > 0 and y < 0 :
    print("4")
elif x < 0 and y > 0 :
    print("2")
else :
    print("3")