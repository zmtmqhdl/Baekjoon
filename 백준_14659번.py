n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
max_num = 0 # ���� ���� ���츮�� ������ ������ max_num���� �ʱ�ȭ
count = 0 # ���� ������ �� �ִ� ���츮�� ������ ������ count���� �ʱ�ȭ
max_count = 0 # ���� ���� ������ �� �ִ� ���츮�� ������ ������ max_count���� �ʱ�ȭ
for i in data : # data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i > max_num : # ���ǹ� if, else -> i��° ���츮�� max_num���츮���� ���� ���
        max_num = i # max_num�� i�� ���� -> ���� ���� ���츮 ����
        count = 0 # count���� �ʱ�ȭ
    else : # i��° ���츮�� max_num���츮���� ���� ���
        count += 1 # count = count + 1
    max_count = max(count, max_count) # max�� ����Ͽ� count, max_count �� ���� ���� max_count�� ����
print(max_count) # ���