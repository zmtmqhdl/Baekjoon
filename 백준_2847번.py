n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ� 
    data.append(int(input())) # append�� ����Ͽ� ���Ե� ���� data��� list�� ���ҷ� �߰�
count = 0 # ������� ������ count���� �ʱ�ȭ
for i in range(n - 2, -1, -1) : # �ݺ��� for -> n - 2���� 0���� -1�� ���ҽ�Ű�� ���ʴ�� i�� �����ϸ� �ݺ�
    if data[i] >= data[i + 1] : # ���ǹ� if -> ���޵Ǵ� ������ �� ���� �ܰ谡 ���� ���
        count += data[i] - data[i + 1] + 1 # count = count + data[i] - data[i + 1] + 1
        data[i] = data[i + 1] - 1 # ���޵Ǵ� ������ ���� �ܰ迡�� ���޵Ǵ� �������� 1�� ����
print(count) # ���