n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(input())) # append�� ����Ͽ� ���Ե� ���� data��� list�� ���ҷ� �߰�
data.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
total = sum(data) # sum�� ����Ͽ� data��� list�� ������ ���� total������ ����
for i in range(0, len(data)) : # �ݺ��� for -> 0���� len(data) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    if i % 3 == 2 : # ���ǹ� if -> 3���� �������� �Ͽ� ���� ������ ���� ���ֱ� ���ؼ� ������ ���� ����
        total -= data[i] # total = total - data[i] -> ���� �߿��� ���� ������ ���� ���� ����
print(total) # ���