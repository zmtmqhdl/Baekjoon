n = int(input()) # �� ����
count = 1 # ������ ���� -> �Է°��� �׻� 1 �̻�
result = 1 # ����� -> �Է°��� �׻� 1 �̻�
while n > count : # �ݺ��� while -> n�� count���� Ŭ ���� �ݺ�
    count += 6 * result # count = count + (6 * result)
    result += 1 # result = result + 1
print(result) # ���