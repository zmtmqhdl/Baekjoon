t = int(input()) # �� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
    data.remove(max(data)) # remove�� max�� ����Ͽ� data��� list���� ���� ū ���� ���Ҹ� ����
    data.remove(min(data)) # remove�� min�� ����Ͽ� data��� list���� ���� ���� ���� ���Ҹ� ����
    if max(data) - min(data) >= 4 : # ���ǹ� if -> �ְ����� �������� �� ������ 3�� ������ �ְ����� �������� ���̰� 4�� �̻��� ���
        print('KIN') # ���
    else : # �ְ����� �������� �� ������ 3�� ������ �ְ����� �������� ���̰� 3�� ������ ���
        print(sum(data)) # ���