n = int(input()) # �� ����
count = 0 # count �ʱ�ȭ
num = 666 # 666�� �� ���� ù ��° ���ڸ� ������ ���� ���� num����
while True : # �ݺ��� While -> False�� �ݺ��� ������ �ݺ�
    if '666' in str(num) : # ���ǹ� if -> str(num)�� 666�� ���ԵǾ����� ���
        count += 1 # count = count + 1
    if count == n : # ���ǹ� if -> count�� n�� ���� ���� ���
        print(num) # ���
        break # ����
    num += 1 # num = num + 1