while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    try : # ���������� ������ ���
        print(input()) # �Էµ� ���� ���
    except EOFError : # ���ܰ� �߻��� ���
        break # ����