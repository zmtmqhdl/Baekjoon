t = int(input()) # �׽�Ʈ Ƚ�� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    n = int(input()) # �� ����
    data = list(map(str, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
    for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
        if i == 0 : # ���ǹ� if, elif
            result = data[0] # result��� ������ data[0]������ �ʱ�ȭ
        elif ord(data[i]) > ord(result[0]) : # ord�� ����Ͽ� �����ڵ尪�� ��
                                             # result[0]�� ���� data[i]�� ���� ���Ͽ� data[i]�� ���� Ŭ ���
            result = result + data[i] # data[i]�� �ڿ� ����
        elif ord(data[i]) <= ord(result[0]) : # ord�� ����Ͽ� �����ڵ尪�� ��
                                             # result[0]�� ���� data[i]�� ���� ���Ͽ� data[i]�� ���� ���� ���
            result = data[i] + result # data[i]�� �տ� ����
    print(result) # ���