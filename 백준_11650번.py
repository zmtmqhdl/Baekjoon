n = int(input()) # �׽�Ʈ Ƚ�� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    x, y = map(int, input().split()) # �� ����
    data.append((x, y)) # append�� ����Ͽ� data��� list�� tuple���·� x�� y���� ���ҷ� �߰�
data.sort() # sort�� ����Ͽ� data��� list�� ������������ ����
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� i�� ���ʴ�� ����
    print(i[0], i[1]) # tuple���� �����Ͽ� ���