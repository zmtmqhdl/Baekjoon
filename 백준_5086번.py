while True : # �ݺ��� for -> False�� ��ȯ�� ������ �ݺ�
    a, b = map(int, input().split()) # �� ����
    if a == 0 and b == 0 : # ���ǹ� if -> ������ �ٿ� 0�� 2�� �־��� ���
        break # �ݺ��� ����
    if b % a == 0 : # ���ǹ� if, elif, else -> ù ��° ���ڰ� �� ��° ������ ����� ���
        print('factor') # ���
    elif a % b == 0 : # ù ��° ���ڰ� �� ��° ������ ����� ���
        print('multiple') # ���
    else : # ù ��° ���ڰ� �� ��° ������ ����� ��� ��� �ƴ� ���
        print('neither') # ���