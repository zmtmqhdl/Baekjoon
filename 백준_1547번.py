n = int(input()) # �� ����
cup = [1, 2, 3] # ���� ��ġ�� ������ cup�̶�� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    x, y = map(int, input().split()) # �� ����
    xi = cup.index(x) # ���� ��ġ index���� xi��� ������ ����
    yi = cup.index(y) # ���� ��ġ index���� yi��� ������ ����
    cup[xi], cup[yi] = cup[yi], cup[xi] # �ų����� ��ġ ��ȯ
print(cup[0]) # ���