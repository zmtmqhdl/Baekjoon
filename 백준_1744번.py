n = int(input()) # �׽�Ʈ Ƚ�� ����
result = 0 # ������� ������ result���� �ʱ�ȭ
plus = [] # ����� ������ plus��� list����
minus = [] # ������ 0�� ������ minus��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data = int(input()) # �� ����
    if data == 1 : # ���ǹ� if, elif -> data�� 1�� ���� ������ ���ؾ� ��
        result += 1 # result = result + 1
    elif data > 0  : # data�� ����� ���
        plus.append(data) # append�� ����Ͽ� data�� plus��� list�� ���ҷ� ����
    elif data <= 0 : # data�� ���� �Ǵ� 0�� ���
        minus.append(data) # append�� ����Ͽ� data�� minus��� list�� ���ҷ� ����
plus.sort() # sort�� ����Ͽ� plus��� list�� ������������ ����
minus.sort() # sort�� ����Ͽ� minus��� list�� ������������ ����
if len(plus) % 2 == 1 : # ���ǹ� if, elif -> plus��� list�� ������ ������ Ȧ���� ���
    result += plus[0] # result = result + plus[0] -> ���� ���� ���� result�� ����
    del plus[0] # ���� ���� ���� plus��� list���� ����
    for i in range(0, len(plus), 2) : # �ݺ��� for -> 0���� len(plus) - 1���� 2�� �������� �ΰ� i�� ���ʴ�� �����ϸ� �ݺ�
        result += plus[i] * plus[i + 1] # result = result + (plus[i] * plus[i + 1]) -> 2���� ��� ���� �� result�� ����
elif len(plus) % 2 == 0 : # plus��� list�� ������ ������ ¦���� ���
    for i in range(0, len(plus), 2) : # �ݺ��� for -> 0���� len(plus) - 1���� 2�� �������� �ΰ� i�� ���ʴ�� �����ϸ� �ݺ�
        result += plus[i] * plus[i + 1] # result = result + (plus[i] * plus[i + 1]) -> 2���� ��� ���� �� result�� ����
if len(minus) % 2 == 1 : # ���ǹ� if, elif -> minus��� list�� ������ ������ Ȧ���� ���
    result += minus[-1] # result = result + minus[0] -> ���� ���� ���� result�� ����
    del minus[-1]  # ���� ���� ���� minus��� list���� ����
    for i in range(0, len(minus), 2) : # �ݺ��� for -> 0���� len(minus) - 1���� 2�� �������� �ΰ� i�� ���ʴ�� �����ϸ� �ݺ�
        result += minus[i] * minus[i + 1] # result = result + (minus[i] * minus[i + 1]) -> 2���� ��� ���� �� result�� ����
elif len(minus) % 2 == 0 : # minus��� list�� ������ ������ ¦���� ���
    for i in range(0, len(minus), 2) : # �ݺ��� for -> 0���� len(minus) - 1���� 2�� �������� �ΰ� i�� ���ʴ�� �����ϸ� �ݺ�
        result += minus[i] * minus[i + 1] # result = result + (minus[i] * minus[i + 1]) -> 2���� ��� ���� �� result�� ����
print(result) # ���