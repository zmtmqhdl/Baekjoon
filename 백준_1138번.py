n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
line = [0] * n # ���� ������ ������ [0] * n������ line�̶�� list����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    count = 0 # line�̶�� list���� ���õ� ��ġ�� �� ��° index���� �˱� ���� count���� �ʱ�ȭ
    for j in range(n) : # �ݺ��� for -> 0���� n - 1���� ���ʴ�� j�� �����ϸ� �ݺ�
        if count == data[i] and line[j] == 0 : # ������ if, elif -> ���ʿ� ����� �ִ� ���� �����鼭 �ڸ��� ����ִ� ���
            line[j] = i + 1 # �ڸ��� ����� ��ġ
            break # ����
        elif line[j] == 0 : # �ڸ��� ������� ���� ���
            count += 1 # count = count + 1
print(' '.join(map(str, line))) # ���