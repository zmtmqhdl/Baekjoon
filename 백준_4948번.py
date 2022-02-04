num = 123456 * 2 + 1 # n�� �ִ���� + 1 -> list������ ���� ����
data = [True] * num # True���� ���� num���� ���Ҹ� ���� data��� list����
                    # data�� �ش� �ε��� ���� True�̸� �Ҽ�, False�̸� �Ҽ��� �ƴ�
for i in range(2, int(num ** 0.5) + 1) : # �ݺ��� for -> num ** 0.5�� ������
    if data[i] == True : # ���ǹ� if -> �Ҽ� �Ǻ�
        for j in range(2 * i, num, i) : # �ݺ��� for -> 2 * i���� num���� i�� �������� j�� ���ʴ�� ����
            data[j] = False
def prime_count(n) : # �Լ� ����
    count = 0 # �Ҽ� ������ ����ϱ� ���� count���� �ʱ�ȭ
    for i in range(n + 1, n * 2 + 1) : # �ݺ��� for
        if data[i] == True : # ���ǹ� if -> i�� �Ҽ����
            count += 1 # count = count + 1
    print(count) # ���
while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    n = int(input()) # �� ����
    if n == 0 : # ���ǹ� if
        break # ����
    prime_count(n) # pirme_count�Լ��� n����
#�����佺�׳׽��� ü