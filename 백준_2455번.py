data = [] # data��� list����
for _ in range(4) : # �ݺ��� for -> 4ȸ �ݺ�
    x, y = map(int, input().split()) # �� ����
    data.append([x, y]) # append�� ����Ͽ� [x, y]�� ���� data��� list�� 2�� �迭���·� ����
max = 0 # ������� ������ cnt��� ���� �ʱ�ȭ
human = 0 # ����� ���� ������ human�̶�� ���� �ʱ�ȭ
for i in range(4) : # �ݺ��� for -> 0���� 3���� i�� ���ʴ�� �����ϸ� �ݺ�
    human += data[i][1] # human = human + data[i][0] -> ������ ź ���
    human -= data[i][0] # human = human - data[i][1] -> �������� ���� ���
    if human > max : # ���ǹ� if -> ���� ������ ź ����� ������ ������ ���� ��� ������ ���� ���
        max = human # max���� human���� ����
print(max) # ���