n = int(input()) # �� ����
road_data = list(map(int, input().split())) # �� ����
cost_data = list(map(int, input().split())) # �� ����
min_price = cost_data[0] # �������� �ּڰ��� ������ min_pirce���� ���� �� cost_data[0]�� �� ����
sum = 0 # ����� ���� ������ sum���� �ʱ�ȭ
for i in range(len(road_data)) : # �ݺ��� for -> 0���� len(road_data) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    if cost_data[i] >= min_price : # ���ǹ� if, elif -> ���� ������ ������ ���ݺ��� ���� �ӹ� �������� ������ �� ������ ���
        sum += min_price * road_data[i] # sum = sum + (min_price * road_data[i])
    elif cost_data[i] < min_price : # ���� ������ ������ ������ ���� �ӹ� �������� ���ݺ��� ������ ���
        min_price = cost_data[i] # �������� �ּڰ� ����
        sum += min_price * road_data[i] # sum = sum + (min_price * road_data[i])
print(sum) # ���