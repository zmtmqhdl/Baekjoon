n = int(input()) # �� ����
for i in range(1, n + 1) : # �ݺ��� for -> 1���� n���� i�� ���ʴ�� �����ϸ� �ݺ�
    result = ' ' * (n - i) + '*' * ((2 * i) - 1) # ����
    print(result) # ���