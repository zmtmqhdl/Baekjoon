n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
count = 0 # ������� ������ count���� �ʱ�ȭ
milk = 0 # ������ ������ ������ milk���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i == milk : # ���ǹ� if -> i�� milk�� ��ġ�� ���
        count += 1 # count = count + 1
        milk += 1 # milk = milk + 1
        if milk == 3 : # ���ǹ� if -> �ٳ��� ������ ������ ���
            milk = 0 # ���� ������ ���ž� �ϴ� ���� ����
print(count) # ���