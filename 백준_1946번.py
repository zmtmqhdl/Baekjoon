import sys # ���̺귯�� ȣ��
t = int(sys.stdin.readline()) # �׽�Ʈ Ƚ�� ���� -> sys.stdin.readline() = input()
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    n = int(sys.stdin.readline()) # �� ����
    data = [] # data��� list����
    count = 1 # ġ�� �� �� �ִ� ���� ����� ���� ������ count���� ����
    for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
        x, y = map(int, sys.stdin.readline().rstrip().split()) # �� ����
        data.append([x, y]) # append�� ����Ͽ� [x, y]�� data��� list�� ���ҷ� �߰�
    data.sort() # sort�� ����Ͽ� data��� list�� ������������ ����
    check = data[0][1] # ���� ������ ���ϱ� ���� check������ �����ϰ� ���� ������ 1���� ����� ���� ������ ����
    for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� i�� ������� �����ϸ� �ݺ�
        if check > data[i][1] : # ���ǹ� if -> ���� ���� ��
            count += 1 # count = count + 1
            check = data[i][1] # �� ����� data[i][1]�� ��ü
    print(count) # ���