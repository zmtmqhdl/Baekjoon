while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    a = list(map(int, input().split())) # �� ����
    high = max(a) # ���� ū ���� high��� ������ ����
    if sum(a) == 0 : # ���ǹ� if -> 0 0 0�� �Է��� ���
        break # ����
    a.remove(high) # remove�� ����� high���� a��� list���� ����
    if high ** 2 == a[0] ** 2 + a[1] ** 2 : # ��Ÿ����� ���� ����
        print("right") # ���
    else :
        print("wrong") # ����