t = int(input()) # �׽�Ʈ Ƚ�� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    n = int(input()) # �� ����
    data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
    data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
    result = 0 # ������� ������ result���� �ʱ�ȭ
    for i in range(2, n) : # �ݺ��� for -> 2���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
        result = max(result, abs(data[i] - data[i - 2])) # �� �볪�� ���� ������ �� ����
                                                         # �볪������ ���� �� index���̸� 2�� �ΰ� ����
                                                         # ó�� �볪�� 1 2 3 4 5
                                                         # ���� �볪�� 4 2 1 3 5
    print(result) # ���