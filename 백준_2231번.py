n = int(input()) # �� ����
result = 0 # ������� ������ result���� ����
for i in range(1, n + 1) : # �ݺ��� for -> 1���� n������ ���� i�� ���ʴ�� �����ϸ� �ݺ�
    data = list(map(int, str(i))) # str(i)�� ���� int������ �ٲ� �� ���ھ��� ���ҷ� ���� data��� list����
    result = i + sum(data) # i�� i�� �̷�� �� �ڸ����� ��
    if result == n : # ���ǹ� if -> ������ ���ǿ� �ش�ȴٸ�
        print(i) # ���
        break # ����
    if i == n : # ���ǹ� if -> �����ڰ� �������� ���� ���
        print(0) # ���