data = input() # �� ����
data = data.replace('XXXX', 'AAAA') # replace�� ����Ͽ� XXXX�� AAAA�� ��ü
data = data.replace('XX', 'BB') # replace�� ����Ͽ� XX�� BB�� ��ü
if 'X' in data : # ���ǹ� if, else -> X�� 1���� �����ִ� ���
    print(-1) # ���
else : # X�� ��� ��ȯ�Ǿ��� ���
    print(data) # ���