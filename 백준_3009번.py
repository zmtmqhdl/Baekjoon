x_list = [] # x������ ������ x_list��� list����
y_list = [] # y������ ������ y_list��� list����
for _ in range(3) : # �ݺ��� for
    x, y = map(int, input().split()) # �� ����
    x_list.append(x) # x_list��� list�� x���� ���ҷ� �߰�
    y_list.append(y) # y_list��� list�� y���� ���ҷ� �߰�
for i in range(3) : # �ݺ��� for
    if x_list.count(x_list[i]) == 1: # ������ if -> count�� ����Ͽ� x_list�� ���� ���� �� ������ 1���� ���� ã�Ƴ�
        result_x = x_list[i]
    if y_list.count(y_list[i]) == 1: # ������ if -> count�� ����Ͽ� y_list�� ���� ���� �� ������ 1���� ���� ã�Ƴ�
        result_y = y_list[i]
print(result_x, result_y) # ���