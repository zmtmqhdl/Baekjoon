n = int(input()) # �� ����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    print(' ' * i + '*' * (2 * (n - i) - 1)) # ���