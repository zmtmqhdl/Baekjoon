n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
print(data[(n - 1) // 2]) # ���
                          # data��� list���� index�� ���� len(data) // 2�� ���� ����
                          # ���� ���� ���� ����� ��� ���� ���� ���� ����ϹǷ� len(data)�� ¦���� ���� n - 1�� �ذ�