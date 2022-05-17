import sys # ���̺귯�� ȣ��
n = int(sys.stdin.readline()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    command = sys.stdin.readline().split() # �� ����
    if command[0] == 'push' : # ���ǹ� if, elif, else -> ��ɾ push�� ���
        data.append(command[1]) # append�� ����Ͽ� command[1]�� data��� list�� ���ҷ� �߰�
    elif command[0] == 'pop' : # ��ɾ pop�� ���
        if len(data) == 0 : # ���ǹ� if, else -> ������ �� ���
            print(-1) # ���
        else : # ������ ������� ���� ���
            print(data.pop()) # pop�� �̿��Ͽ� ���� ���� �ִ� ������ ���� ���
    elif command[0] == 'size' : # ��ɾ size�� ���
        print(len(data)) # len�� ����Ͽ� data��� list�� ������ ������ ���
    elif command[0] == 'empty' : # ��ɾ empty�� ���
        if len(data) == 0 : # ���ǹ� if, else -> ������ �� ���
            print(1) # ���
        else : # ������ ������� ���� ���
            print(0) # ���
    else : # ��ɾ top�� ���
        if len(data) != 0 : # ���ǹ� if, else -> ������ ������� ���� ���
            print(data[-1]) # ���
        else : # ������ �� ���
            print(-1) # ���