data = [] # data��� list����
for _ in range(5) : # �ݺ��� for -> 5ȸ �ݺ�
    n = int(input()) # �� ����
    if n < 40 : # ���ǹ� if -> n�� 40�̸��� ���
        n = 40 # n�� ���� 40���� ����
    data.append(n) # append�� ����Ͽ� data��� list�� n�� ���� ���ҷ� ����
print(int(sum(data) / 5)) # ��� ���