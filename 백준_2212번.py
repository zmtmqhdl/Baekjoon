n = int(input()) # �� ����
k = int(input()) # �� ����
data = sorted(list(map(int, input().split()))) # ���Ե� ���� ���ҷ� ���� data��� ����
                                               # sorted�� ����� ���Ե� ���Ҹ� ������������ ����
if k >= n : # ���ǹ� if, else -> ���߱��� ���� �������� ���� ���
    print(0) # ���
else :
    dist = [] # dist��� list����
    for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
        dist.append(data[i] - data[i - 1]) # append�� ����Ͽ� data[i] - data[i - 1]���� dist��� list�� ���ҷ� ����
    dist.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� dist��� list�� ���Ҹ� ������������ ����
    for _ in range(k - 1) : # �ݺ��� for -> k - 2�� �ݺ�
        dist.pop(0) # pop�� ����Ͽ� 0��° index�� ���� dist��� list���� ����
    print(sum(dist)) # sum�� ����Ͽ� dist��� list�� ������ ���� ���