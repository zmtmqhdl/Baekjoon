n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
count = 0 # count���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i == n : # ���ǹ� if -> i�� n�� ���� ���� ���
        count += 1 # count = count + 1
print(count) # ���