t = int(input()) # �׽�Ʈ Ƚ�� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # �� ����
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) # �������� ���ȯ ������ �Ÿ�
    data = [r1, r2, distance] # r1, r2, distacne�� ���Ҹ� ���� data��� list����
    m = max(data) # max�� ����ؼ� data��� list���� ���� ū ���� ���� ���Ҹ� m�̶�� ������ ����
    data.remove(m) # append�� ����ؼ� data��� list���� m�� ����
    if distance == 0 and r1 == r2 : # ���ǹ� if, elif, else -> ������ ��ġ ����
                                    # �������� ���ȯ�� ���� ��ġ�� �ִ� ���
        print(-1) # ���
    elif distance == r1 + r2 or m == sum(data) : # �������� ������ ���ȯ�� ������ 1���� �������� ��ĥ ���
        print(1) # ���
    elif m > sum(data) : # �������� ������ ���ȯ�� ������ ������ ���� ���
        print(0) # ���
    else : # �������� ������ ���ȯ�� ������ 2���� ������ ��ĥ ���
        print(2) # ���