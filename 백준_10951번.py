while True :  # False�� �� ������ �ݺ�
    try : # ���� ó�� try, except -> try�� �����ų �ڵ�
        a, b = map(int, input().split()) # �� ����
        print(a + b) # ���
    except : # a, b�� int���� �ƴ� �ٸ� ���� ���� �����ų �ڵ�
             # try�ι����� ���� �߻��� �����ų �ڵ�
        break # �ݺ��� ����