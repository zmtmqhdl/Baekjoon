def isPrime() : # �Լ� ����
    data = [False, False] + [True] * 9999 # data��� list ����
                                          # 0, 1��° index�� ���� False�̰� �� ������ ������ True
                                          # data�� �ش� �ε��� ���� True�̸� �Ҽ�, False�̸� �Ҽ��� �ƴ�
    for i in range(2, int(10001 ** 0.5) + 1) : # �ݺ��� for -> 10001 ** 0.5�� ������
        if data[i] == True : # ���ǹ� if -> �Ҽ� �Ǻ�
            for j in range(2 * i, 10001, i) : # �ݺ��� for -> 2 * i���� 10001���� i�� �������� j�� ���ʴ�� ����
                data[j] = False
    t = int(input()) # �׽�Ʈ Ƚ�� ����
    for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
        n = int(input()) # �� ����
        a = n // 2 # �� �Ҽ��� ���̸� ���� �۰� �ϱ� ���ؼ� n // 2 
        b = n // 2 # �� �Ҽ��� ���̸� ���� �۰� �ϱ� ���ؼ� n // 2
        for _ in range(10000) : # �ݺ��� for
            if data[a] == True and data[b] == True: # ���ǹ� if -> a�� b�� �Ҽ����� �Ǻ�
                print(a, b) # ���
                break # ����
            a -= 1 # a = a - 1
            b += 1 # b = b + 1
                   # a�� 1������Ű�� b�� 1���ҽ�Ű�� a + b = n ����
isPrime() # �Լ� ����