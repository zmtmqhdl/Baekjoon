n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    a, b = map(int, input().split()) # �� ����
    data.append([a, b]) # data��� list�� [a, b]�� ���ҷ� �߰�
data.sort(key = lambda x : (x[0], x[1])) # sort(key = lambda x : (x[0], x[1]))
time = data[0][0] + data[0][1] # �Ұ� �����ϴµ� �ɸ��� �ð��� �����ϱ� ���� ���� time����
                               # ó�� �����ϴ� ���� �ð��� time������ ����
for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    if time >= data[i][0] : # ���� ������ ���� �����ð����� ������ �ҵ��� ������ �ð����� ���� ��� 
        time += data[i][1] # time = time + data[i][1]
                           # ������ �ð� + ���� ������ ���� �˼� �ð�
    else : # ���� ������ ���� �����ð��� ������ �Ұ� �˼��ް� ������ �ð����� ū ���
        time = data[i][0] + data[i][1] # time���� ����
print(time) # ���