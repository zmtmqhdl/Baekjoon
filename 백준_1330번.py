a, b = map(int, input().split()) # map(적용시킬 함수, 적용할 값)
if a > b : # 조건문 if, elif, else
    print(">") # 출력
elif a < b :
    print("<")
else :
    print("==")