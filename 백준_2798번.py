n, m = map(int, input().split()) # �� ����
card = list(map(int, input().split())) # �Էµ� ���� ���� card��� list����
sum = 0 # ���õ� 3���� ī���� ���� ������ sum�̶�� ���� ����
for a in card : # �ݺ��� for -> card�� ���Ҹ� ���ʴ�� a�� ����
    for b in card : # �ݺ��� for -> card�� ���Ҹ� ���ʴ�� b�� ����
        for c in card : # �ݺ��� for -> card�� ���Ҹ� ���ʴ�� c�� ����
            if a != b and b != c and a != c and a + b + c > sum and a + b + c <= m : # ���ǹ� if -> a, b, c�� ���� ���� �ٸ��� a, b, c�� ���� ������ sum���� ũ�� m���� �۰ų� ���ٸ�
                sum = a + b + c # sum�� ���ο� a + b + c�� ����
print(sum) # ���