n = int(input()) # �׽�Ʈ Ƚ�� ����
data = [] # data��� list����
for _ in range(n): # �ݺ��� for -> n��ŭ �ݺ�
    x, y = map(int, input().split()) # �� ����
    data.append((x, y)) # append�� ����Ͽ� x, y�� data��� list�� ���ҷ� ����
for i in data: # �ݺ��� for -> i�� data�� ���Ҹ� ���ʴ�� ����
    rank = 1 # ���� �ʱ�ȭ
    for j in data: # �ݺ��� for -> j�� data�� ���Ҹ� ���ʴ�� ����
        if i[0] < j[0] and i[1] < j[1]: # ���ǹ� if -> i�� x, y�� ���� j�� x, y������ ���� ���
                                        # i���� j�� ��ġ�� ū ���
                rank += 1 # rank = rank + 1
    print(rank, end = " ") # end�� ����Ͽ� ������� ���