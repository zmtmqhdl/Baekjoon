k = int(input()) # �� ����
data = [] # data��� list����
for _ in range(k) : # �ݺ��� for -> k��ŭ �ݺ�
    a = int(input()) # �� ����
    if a == 0 : # ���ǹ� if, else -> �����̰� 0�� ��ģ ���
        del data[-1] # del�� ����Ͽ� data��� list���� ���� ������ ���Ҹ� ����
    else : # �����̰� 0�� ��ġ�� ���� ���
        data.append(a) # append�� ����Ͽ� data��� list�� a�� ���ҷ� ����
print(sum(data)) # sum�� ����Ͽ� data��� list�� ������ ���� ���