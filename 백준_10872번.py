n = int(input()) # �� ����
result = 1 
if n == 0 : # ���ǹ� if, else
    result = 1
else :
    for i in range(1, n + 1) : # �ݺ��� for ->  i�� 1���� n���� ���ʴ�� ���� 
        result *= i # result = result * i
print(result) # ���