n = list(input().split('-')) # split�� ����Ͽ� ���Ե� ���� -�� �������� ���� ���� ���ҷ� ���� n�̶�� list����
sum = 0 # ��� ����� ������ sum���� �ʱ�ȭ
for i in range(0, len(n)) : # �ݺ��� for -> 0���� len(n) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    temp = n[i].split('+') # split�� ����Ͽ� n[i]�� +�� �������� ���� ���� temp�� ����
    if i == 0 : # ���ǹ� if -> ù -�� ������ ������ ��� ���� ������ ��
        for j in temp : # ���ǹ� if -> temp��� list�� ���Ҹ� ���ʴ�� j�� �����ϸ� �ݺ�
            sum += int(j) # sum = sum + int(j)
    else : # ó���� ���Ե� ������ -�� �������� �������� ������ n[0]�� ������ ��� ������ ������ �� 
        for j in temp : # ���ǹ� if -> temp��� list�� ���Ҹ� ���ʴ�� j�� �����ϸ� �ݺ�
            sum -= int(j) # sum = sum - int(j)
print(sum) # ���