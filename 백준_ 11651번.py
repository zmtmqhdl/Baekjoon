n = int(input()) # �׽�Ʈ Ƚ�� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    x, y = map(int, input().split()) # �� ����
    data.append((y, x)) # append�� ����Ͽ� data��� list�� tuple���·� x�� y���� ���ҷ� �߰�
                        # y���� �켱������ ������������ ���ĵǾ�� �ϹǷ� (y, x)
data.sort() # sort�� ����Ͽ� data��� list�� ������������ ����
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� i�� ���ʴ�� ����
    print(i[1], i[0]) # data���� (y, x)���� ���·� ���Ұ� �� �����Ƿ� y, x�� ������ ����Ͽ� tuple���� �����Ͽ� ���