n, m = map(int, input().split()) # �� ����
sum = 0 # ����� ������ sum���� �ʱ�ȭ
data = [] # data��� list����
for _ in range(m) : # �ݺ��� for -> m��ŭ �ݺ�
    x, y = list(map(int, input().split())) # x, y
    data.append([x, y]) # append�� ����Ͽ� [x, y]�� data��� list�� ���ҷ� �߰�
                        # 2�� �迭 ���·� �����
six_data = sorted(data, key = lambda x : x[0]) # sorted(data, key = lambda x : x[0])�� ����Ͽ� data��� list�� ���Ҹ� x���� �������� ������������ �����Ͽ� six_data��� list�� ����
                                               # ��Ű�� ������ ������ ������ ����
one_data = sorted(data, key = lambda x : x[1]) # sorted(data, key = lambda x : x[1])�� ����Ͽ� data��� list�� ���Ҹ� y���� �������� ������������ �����Ͽ� six_data��� list�� ����
                                               # ���� ������ ������ ������ ����
if six_data[0][0] <= one_data[0][1] * 6 : # ���ǹ� if, else -> ��Ű���� ������ ������ ���ݺ��� ���ų� ���� ���
    sum = six_data[0][0] * (n // 6) + one_data[0][1] * (n % 6) # n�� 6���� ���� �� * ��Ű�� ���� + n�� 6���� ������ ���� ������ * ���� ����
    if six_data[0][0] < one_data[0][1] * (n % 6) : # ���ǹ� if -> �����ؾ��ϴ� ������ �ʰ��ϴ��� ��Ű���� �����ϴ� ���� ������ ���
        sum = six_data[0][0] * (n // 6 + 1) # (n�� 6���� ���� �� + 1) * ��Ű�� ����
else: # ��Ű���� ������ ������ �����ϴ� �ͺ��� ��� ���
    sum = one_data[0][1] * n # ���� ���� * n
print(sum) # ���