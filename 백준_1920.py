import sys # ���̺귯�� ȣ��
n = int(sys.stdin.readline()) # �� ����
n_data = set(map(int, sys.stdin.readline().split())) # ���Ե� ���� ���ҷ� ���� n_data��� set����
m = int(sys.stdin.readline()) # �� ����
m_data = list(map(int, sys.stdin.readline().split())) # ���Ե� ���� ���ҷ� ���� m_data��� list����
for i in m_data : # �ݺ��� for -> m_data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i in n_data : # ���ǹ� if, else -> i�� n_data��� set�� ���ҷ� �����ϴ� ���
        print(1) # ���
    else : # i�� n_data��� set�� ���ҷ� �������� �ʴ� ���
        print(0) # ���