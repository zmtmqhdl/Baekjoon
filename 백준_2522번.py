n = int(input()) # �� ����
for i in range(1, n + 1) : # �ݺ��� for -> 1���� n���� ���ʴ�� i�� �����ϸ� �ݺ�
    print(' ' * (n - i) + '*' * i) # ���
for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
    print(' ' * i + '*' * (n - i)) # ���