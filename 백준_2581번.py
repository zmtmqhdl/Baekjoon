m = int(input()) # �� ����
n = int(input()) # �� ����
data = [] # data��� list����
for i in range(m, n + 1) : # �ݺ��� for -> m���� n������ ���� i�� ���ʴ�� ����
    count = 0 # �Ҽ��� �Ǻ��ϱ� ���� count���� �ʱ�ȭ
    if i > 1 : # ���ǹ� if -> 1�� �����ϱ� ���ؼ� i > 1
        for j in range(2, i) : # �ݺ��� for -> 2���� i - 1���� ������� j�� ����
            if i % j == 0 : # ���ǹ� if -> i�� �Ҽ��� �ƴ� ���
                count = 1 # i�� �Ҽ��� �ƴ� ���
                break # ����
        if count == 0 : # ���ǹ� if -> i�� �Ҽ��� ���
            data.append(i) # data��� list�� i�� ���ҷ� �߰�
if len(data) > 0 : # ���ǹ� if -> �Ҽ��� ���� ���� ���� ��츦 �Ǵ�
    print(sum(data)) # sum�� Ȱ���� data��� list�� �ִ� ������ ���� ���
    print(min(data)) # min�� Ȱ���� data��� list�� �ִ� ���ҵ� �� �ּҰ��� ���
else : 
    print(-1) # ���