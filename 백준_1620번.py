import sys # ���̺귯�� ȣ��
n, m = map(int, sys.stdin.readline().split()) # �� ����
dict = {} # dict�̶�� dictionary����
for i in range(1, n + 1) : # �ݺ��� for -> 1���� n���� i�� ���ʴ�� �����ϸ� �ݺ�
    a = sys.stdin.readline().rstrip() # �� ����
    dict[i] = a # dict��� dictionary�� ���� ����
    dict[a] = i # dict��� dictionary�� ���� ����
for i in range(m) : # �ݺ��� for -> 0���� m - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    quest = sys.stdin.readline().rstrip() # �� ����
    if quest.isdigit() : # ���ǹ� if -> quest�� ������ ���
        print(dict[int(quest)]) # ���
    else : # quest�� ������ ���
        print(dict[quest]) # ���