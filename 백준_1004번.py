t = int(input()) # �� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    x1, y1, x2, y2 = map(int, input().split()) # �� ����
    n = int(input()) # �� ����
    result = 0 # ������� ������ result���� �ʱ�ȭ
    for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
        px, py, radius = map(int, input().split()) # �� ����
        start = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5 # �༺�߽ɺ��� ������������ �Ÿ�
        end = (((px - x2) ** 2) + ((py - y2) ** 2)) ** 0.5 # �༺�߽ɺ��� ������������ �Ÿ�
        if start < radius and end < radius : # ���ǹ� if, elif -> �������� �������� ��� �� �ȿ� ���� ���
            pass #  # ���
        elif start < radius : # �������� �ȿ� ���� ���
            result += 1 # result = result + 1
        elif end < radius : # �������� �ȿ� ���� ���
            result += 1 # result = result + 1
    print(result) # ���