n = int(input()) # �׽�Ʈ Ƚ�� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    x, y = map(str, input().split()) # �� ����
    data.append((int(x), y)) # append�� ����Ͽ� data�� x, y�� ���ҷ� ����
data.sort(key = lambda x : x[0]) # lamdba�� ����Ͽ� ���� ������������ ����
                                 # lambda �Ű����� : ǥ���� -> �Լ��� �� �ٷ� ǥ���� ��
                                 # lambda x : (x[0], x[1])�� �ϰ� �Ǹ� ���� ��������, �̸� ������������ ���� ����
for i in data : # �ݺ��� for -> i�� daat�� ���Ҹ� ���ʴ�� ����
    print(i[0], i[1]) # i�� 0��° index���� 1��° index���� �и��Ͽ� ������ �ΰ� ���