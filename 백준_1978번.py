n = int(input()) # �� ����
data = list(map(int, input().split())) # �� ����
result = 0 # ��� �ʱ�ȭ
for i in data : # �ݺ��� for -> data�� ���Ҹ� ���ʴ�� i�� ����
    extra_count = 0 # �Ҽ��� �Ǻ��ϱ� ���� extra_count���� �ʱ�ȭ
    if i > 1 : # ���ǹ� if -> 1�� �����ϱ� ���ؼ� i > 1
        for j in range(2, i) : # �ݺ��� for -> 2���� i - 1���� ���ʴ�� j�� ����
            if i % j == 0 : # ���ǹ� if -> i�� �Ҽ��� �ƴ� ���
                extra_count = 1 # i�� �Ҽ��� �ƴ� ���
                break # ����
        if extra_count == 0 : # ���ǹ� if -> i�� �Ҽ��� ���
            result += 1 # result = result + 1
print(result) # ���