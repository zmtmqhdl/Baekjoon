n = m = int(input()) # �� ����
count = 0 # ����� ī��Ʈ
while True : # False�� �� ������ �ݺ�
    num1 = m // 10 # m�� ���ڸ� ��
    num2 = m % 10 # m�� ���ڸ� ��
    new = num1 + num2 # �� �ڸ��� ���ڸ� ����
    m = int(str(num2) + str(new % 10)) # ���ڷ� ���ϱ� ���� int���� str�� ��ȯ�Ͽ� ���ڸ� ��ģ �� �ٽ� int������ ��ȯ
                                       # ���� m�� ���ڸ� �� + new�� ���ڸ� ��
    count += 1 # count = count + 1
    if m == n : # ���ǹ� if
        print(count) # ���
        break # �ݺ��� ����