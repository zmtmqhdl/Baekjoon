t = int(input()) # �׽�Ʈ Ƚ�� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    k = int(input()) # �� ����
    n = int(input()) # �� ����
    people = [i for i in range(1, n + 1)] # 1 ~ n������ ���Ҹ� ���� people�̶�� list ����
    for _ in range(k) : # �ݺ��� for -> k��ŭ �ݺ�
        for i in range(1, n) : # �ݺ��� for -> i�� index�� Ȱ���
            people[i] += people[i - 1] # people[i] = people[i] + people[i - 1]
                                       # �Ʒ����� �������� ��� ���� ��
    print(people[-1]) # �����̽��� �̿��Ͽ� people�̶�� list���� ���� ������ ���� ���