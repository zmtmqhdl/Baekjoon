set = [1, 1, 2, 2, 2, 8] # �ùٸ� ��Ʈ
data = list(map(int, input().split())) # �߰��� �ǽ�
for i in range(6) : # �ݺ��� for -> 0���� 5���� i�� ���ʴ�� �����ϸ� �ݺ�
    print(set[i] - data[i], end = ' ') # end�� ����Ͽ� ���� ���� ���