n = int(input()) # �� ����
score = [0] * 301 # 0�� ���ҷ� 301�� ���� score��� list����
data = [0] * 301 # 0�� ���ҷ� 301�� ���� data��� list����
for i in range(1, n + 1) : # �ݺ��� for -> 1���� n���� ���ʴ�� i�� �����ϸ� �ݺ�
    score[i] = int(input()) # �� ����
data[1] = score[1] # data[1]�� score[1]����
data[2] = score[1] + score[2] # data[2]�� score[1] + score[2]����
for i in range(3, n + 1) : # �ݺ��� for -> 3���� n���� ���ʴ�� i�� �����ϸ� �ݺ�
    data[i] = max(data[i - 3] + score[i - 1] + score[i], data[i - 2] + score[i]) # max�� ����Ͽ� data[i - 3] + score[i - 1] + score[i], data[i - 2] + score[i] �� �� ū ���� data[i]�� ����
print(data[i]) # ���