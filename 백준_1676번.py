import math # ���̺귯�� ȣ��
n = int(input()) # �� ����
n = str(math.factorial(n)) # factorial�� ����Ͽ� n! ����
count = 0 # ������� ������ count���� �ʱ�ȭ
for i in n[::-1] : # �ݺ��� for -> n�� ������ ���ں��� ù ���ڱ��� ���ʴ�� i�� �����ϸ� �ݺ�
    if i != '0' : # ���ǹ� if -> i�� 0�� �ƴ� ���
        break # ����
    count += 1 # count = count + 1
print(count) # ���