import sys # ���̺귯�� ȣ��
n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(sys.stdin.readline())) # append�� ����Ͽ� ���Ե� ���� data��� list�� ���ҷ� ����
data.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
istrue = False # �ﰢ���� ���� �� �ִ��� Ȯ���ϱ� ���� istrue������ False�� ����
for i in range(len(data) - 2) : # �ݺ��� for -> 0���� len(data) - 3���� i�� ���ʴ�� �����ϸ� �ݺ�
    if data[i] < data[i + 1] + data[i + 2] : # ���ǹ� if -> �ﰢ���� ���� �� �ִ� ���
        print(data[i] + data[i + 1] + data[i + 2]) # ���
        istrue = True # �ﰢ���� ���� �� �����Ƿ� istrue������ True�� ����
        break # ����
if istrue == False : # ���ǹ� if -> �ﰢ���� ���� �� ���� ���
    print(-1) # ���