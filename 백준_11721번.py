data = input() # �� ����
while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    if len(data) <= 10 : # len(data)�� ���̰� 10������ ���
        print(data) # ���
        break # ����
    else : # len(data)�� ���̰� 11�̻��� ���
        print(data[:10]) # 1���� 10��° index���ڰ� ���
        data = data[10:] # ����� ���ڸ� ������ ���ڵ��� data�� ����