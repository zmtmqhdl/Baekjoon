a, b = map(int, input().split()) # �� ����
if b - 45 < 0 : # ���ǹ� if, else
    b += 15 # b = b + 15
    a -= 1 # a = a - 1
    if a < 0 :
        a = 23
else :
    b -=45
print(a, b) # ���