import sys # sys���̺귯�� ȣ��
a, b, v = map(int, sys.stdin.readline().split()) # �� ���� -> sys.stdin.readline()�� input()�� ������ �ӵ��� �� ����
result = (v - b) / (a - b) # a - b�θ� ������ �Ǹ� ���� �ö� �� �̲������� �͵� �����ϰ� �ǹǷ� v - b�� a - b�� ������� ��
if result == int(result) : # ���ǹ� if -> ����  result�� int(result)�� ���ٸ� 
                           # ����
    print(int(result)) # result�� int������ ��ȯ�Ͽ� ���
else : # result�� int���� �ƴ϶��
       # ������ �ƴ�
    print(int(result) + 1) # result�� int������ ��ȯ�ϰ� �Ҽ����� �Ϸ�� ����ؾ��ϹǷ� int(result) + 1�� ����Ͽ� ���