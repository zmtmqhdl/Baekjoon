data = [] # data��� list����
for _ in range(7) : # �ݺ��� for -> 7ȸ �ݺ�
    num = int(input()) # �� ����
    if num % 2 == 1 : # ���ǹ� if -> num�� Ȧ���� ���
        data.append(num) # append�� ����Ͽ� num�� data��� list�� ���ҷ� ����
if len(data) == 0 : # ���ǹ� if -> Ȧ���� ���� ���
    print(-1) # ���
else : # Ȧ���� �����ϴ� ���
    print(sum(data)) # sum�� ����Ͽ� data��� list�� ������ ���� ���
    print(min(data)) # min�� ����Ͽ� data��� list�� ���� �� �ּڰ� ���