level = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� level�̶�� list����
n = int(input()) # �� ����
data = [] # score��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    score = 0 # ���Ƹ����� ������ ������ ����score �ʱ�ȭ
    for _ in range(3) : # �ݺ��� for -> 3ȸ �ݺ�
        a = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� a��� list����
        for i in range(3) : # �ݺ��� for -> 0���� 2���� i�� ���ʴ�� �����ϸ� �ݺ�
            score += a[i] * level[i] # score = score + a[i] * level[i]
    data.append(score) # append�� ����Ͽ� data��� list�� score�� ���ҷ� �߰�
print(max(data)) # max�� ����Ͽ� data��� list���� ���� ū ���� ���� ���Ҹ� ���