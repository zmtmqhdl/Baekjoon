chess = [] # chess��� list����
for _ in range(8) : # �ݺ��� for -> 8��ŭ �ݺ�
    chess.append(list(map(str, list(input())))) # append�� ����Ͽ� ���Ե� ���� chess��� list�� ���ҷ� ����
answer = 0 # ������� ������ answer���� �ʱ�ȭ
for i in range(8) : # �ݺ��� for -> 0���� 7���� ���ʴ�� i�� �����ϸ� �ݺ�
    for j in range(8) : # �ݺ��� for -> 0���� 7���� ���ʴ�� j�� �����ϸ� �ݺ�
        if (i + j) % 2 == 0 : # ���ǹ� if -> �Ͼ� ĭ�� ���
            if chess[i][j] == 'F' : # ���� ���� ���
                answer += 1 # answer = answer + 1
print(answer) # ���