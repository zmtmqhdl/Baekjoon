import sys # ���̺귯�� ȣ��
n, k = map(int,sys.stdin.readline().split()) # �� ����
data = list(map(int,sys.stdin.readline().rstrip())) # ���Ե� ���� ���ҷ� ���� data��� list����
result = [] # result��� list����
count = k # ���ڸ� ������ Ƚ���� ������ count��� ������ k�� ����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
    while count > 0 and result : # �ݺ��� while -> count�� 0���� ũ�� result�� True�� ��� �ݺ�
        if result[len(result) - 1] < data[i] : # ���ǹ� if -> result�� ������ ���Ұ� data[i]���� ���� ���
            result.pop() # pop�� ����Ͽ� result��� list�� ���� ������ ���� ����
            count -= 1 # count = count - 1
        else : # result�� ������ ���Ұ� data[i]���� ū ���
            break # ����
    result.append(data[i]) # append�� ����Ͽ� data[i]�� result��� list�� ���ҷ� ����
for i in range(n - k) : # �ݺ��� for -> 0���� n - k - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
    print(result[i], end = "") # ���