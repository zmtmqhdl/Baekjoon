n = int(input()) # �� ����
n_data = set(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� n_data��� set����
m = int(input()) # �� ����
m_data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� m_data��� list����
for i in m_data : # �ݺ��� for -> m_data��� list�� ���Ҹ� i�� ���ʴ�� �����ϸ� �ݺ�
    if i in n_data : # ���ǹ� if, else -> i�� n_data��� set�� ���ҿ� ���Ե� ���
        print(1, end = ' ') # ���
    else : # i�� n_data��� set�� ���ҿ� ���Ե��� ���� ���
        print(0, end = ' ') # ���