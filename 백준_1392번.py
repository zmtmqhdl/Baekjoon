n, q = map(int, input().split()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(input())) # append�� ����Ͽ� data��� list�� ���Ե� ���� ���ҷ� �߰�
for _ in range(q) : # �ݺ��� for -> q��ŭ �ݺ�
    t = int(input()) # �� ����
    for i in range(n) : # �ݺ��� for -> 0���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
        if t < sum(data[:i + 1]) : # ���ǹ� if -> t�� sum(data[:i + 1])���� ���� ���
            print(i + 1) # ���
            break # ����