n = int(input()) # �� ����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data = list(input()) # data��� list����
    sum = 0 # '('�� ������ 1�� ���ϰ� ')'�� ������ -1�� �� ����sum �ʱ�ȭ
    for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
        if i == '(' : # ���ǹ� if, else -> i�� '('�� ���
            sum += 1 # sum = sum + 1
        else : # i�� ')'�� ���
            sum -= 1 # sum = sum - 1
        if sum == -1 : # ���ǹ� if -> '('���� ')'�� �̹� �� ���� ���� ��� 
            print('NO') # ���
            break # ����
    if sum > 0 : # ���ǹ� if, elif -> '('���� ')'�� �� ���� ���� ���
        print('NO') # ���
    elif sum == 0 : # ��ȣ ���ڿ��� �ùٸ� ��ȣ ���ڿ��� ���
        print('YES') # ���