s = input() # �� ����
data = set() # data��� set����
for i in range(len(s)) : # �ݺ��� for -> 0���� len(s) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    for j in range(i, len(s)) : # �ݺ��� for -> i���� len(s) - 1���� j�� ���ʴ�� �����ϸ� �ݺ�
        data.add(s[i:j+1]) # add�� ����Ͽ� s[i:j+1]�� data��� set�� ���ҷ� �߰�
                           # �ߺ��� �߰����� ����
print(len(data)) # ���