n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
young_min = data[n] # �������� ���� ���� ũ���� ������
young_max = data[2 * n - 1] # �������� ���� ū ũ���� ������
print(young_max - young_min) # ���