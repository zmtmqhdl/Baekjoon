n = int(input()) # �� ����
count = 2 # ó�� ������ ���� 2�� �����ϱ� ����
while n != 1 : # �ݺ��� while -> n�� 1�� �ƴ� ��� �ݺ�
    if n % count == 0 : # ���ǹ� if, else -> n�� count�� �����������ٸ�
        n //= count # n = n // count 
        print(count) # ���
    else :
        count += 1 # count = count + 1