n = int(input()) # �׽�Ʈ Ƚ�� ����
for _ in range(n) : # �ݺ��� for
    data = list(map(int, input().split())) # data��� list�� int���� �� ����
    average = sum(data[1:]) / data[0] # ��հ� ����
                                      # data[1:] -> data��� list���� 1�� �ε��� ~ ������ �ε���������� ��
    count = 0 # count �ʱ�ȭ
    for score in data[1:] : # �ݺ��� for -> score��� ���� data��� list���� 1��° �ε��� ������ ��
        if score > average : # ���ǹ� if
                count += 1 # count = count + 1
    result = count / data[0] * 100 # ��� ����
    print(f'{result:.3f}%') # f-string�� ����Ͽ� �Ҽ� 3���� �ڸ����� ���
                            # print(f'{��:.ǥ���� �Ҽ� �ڸ���f}') -> ǥ���� �Ҽ� �ڸ������� �Ҽ��� ǥ��