n = int(input()) # �׽�Ʈ Ƚ�� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    new_data = input() # �� ����
    if new_data not in data : # ������ if -> data��� list�� new_data�� ���� ���ٸ�
        data.append(new_data) # append�� ����Ͽ� data��� list�� new_data�� ���ҷ� �߰�
data.sort() # data��� list�� ������������ ����
data.sort(key = len) # data��� list�� ������ ���̰� ���������� �ǵ��� ����
                     # key = len�� ����ϸ� ������ ���̰� ª�� �ͺ��� ������ ��
print(data) # ���