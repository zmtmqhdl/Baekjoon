n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(list(map(int, input().split()))) #append�� ����Ͽ� ���Ե� list�� data��� list�� ���ҷ� �߰�
for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
    for j in range(i + 1) : # �ݺ��� for -> 0���� i���� ������� j�� �����ϸ� �ݺ�
        if j == 0 : # ���ǹ� if, elif, else -> �� ������ ���� ���õ� ���
            data[i][j] += data[i - 1][j] # data[i][j] = data[i][j] + data[i - 1][j]
        elif i == j : # �� �������� ���� ���õ� ���
            data[i][j] += data[i - 1][j - 1] # data[i][j] = data[i][j] + data[i - 1][j - 1]
        else : # �밢�� ���ʰ� �밢�� �������� �� �߿��� ū ���� ����
            data[i][j] += max(data[i - 1][j], data[i - 1][j - 1]) # data[i][j] = data[i][j] = data[i][j] + max(data[i - 1][j], data[i - 1][j - 1])
print(max(data[n - 1])) # ���