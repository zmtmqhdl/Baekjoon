m, n = map(int, input().split()) # �� ����
def isprime(m, n) : # �Լ� ����
    n += 1 # n = n + 1
    data = [True] * n # True���� ���� n���� ���Ҹ� ������ data��� list����
                      # data�� �ش� �ε��� ���� True�̸� �Ҽ�, False�̸� �Ҽ��� �ƴ�
    for i in range(2, int(n ** 0.5) + 1) : # �ݺ��� for -> n ** 0.5�� ������
        if data[i] == True : # ���ǹ� if
            for j in range(2 * i, n, i) : # �ݺ��� for -> 2 * i���� n���� i�� �������� j�� ���ʴ�� ����
                data[j] = False
    for i in range(m, n) : # �ݺ��� for
        if i > 1 and data[i] == True : # ���ǹ� if -> 1�� �Ҽ��� �ƴϹǷ� 1 > 1
            print(i) # ���   
isprime(m, n) # �Լ� ����
# �����佺�׳׽��� ü