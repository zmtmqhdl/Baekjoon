n = int(input()) # �� ����
blank = 0 # ������ ��Ÿ���� ���� blank���� �ʱ�ȭ
while n != 0 : # �ݺ��� while -> n�� 0�� �ƴ� ��� �ݺ�
    print(' ' * blank + '*' * n) # ���
    n -= 1 # n = n - 1
    blank += 1 # blank = blank + 1