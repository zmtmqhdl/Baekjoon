import sys # ���̺귯�� ȣ��
n, k = map(int, sys.stdin.readline().split()) # �� ���� -> sys.stdin.readline().split() = input().split()
plug = [0] * n # 0�� n�� ���� plug��� list����
               # 0�� ���� ���� ���� �÷���
data = list(map(int, sys.stdin.readline().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
count = swap = num = max = 0 # ������� ������ count����, �ٲ� ���� ������ swap����, data��� list�� index���� ������ num����, data��� list�� index���� ������ max���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� i�� ���ʴ�� �����ϸ� �ݺ�
    if i in plug : # ���ǹ� if, elif, else -> i�� ���� plug��� list�� ������ ���
        pass # ������ �ڵ尡 ����
    elif 0 in plug : # plug��� list�� 0�� ������ ���
        plug[plug.index(0)] = i # index�� ����Ͽ� plug��� list�� ���� ó������ ������ 0�� i�� �ٲ�
    else : # ��� �÷��װ� ���� �� ���
        for j in plug : # �ݺ��� for -> plug��� list�� ���Ҹ� j�� ���ʴ�� �����ϸ� �ݺ�
            if j not in data[num:] : # ���ǹ� if, elif -> data[num:]��� list�� j�� ���� �������� ���� ���
                                     # �ش� �����ǰ�� ���߿� �ٽ� ������ ���� ���
                swap = j # ���� ������ �����ǰ swap������ ����
                break # ����
            elif data[num:].index(j) > max : # data��� list���� �� ���߿� ���Ǵ� �����ǰ�� ã�� ����
                max = data[num:].index(j) # �� ���߿� ���Ǵ� �����ǰ�� max������ ����
                swap = j # ���� ������ �����ǰ sawp������ ����
        plug[plug.index(swap)] = i # index�� ����Ͽ� plug��� list�� swap��°�� �ִ� ���� i�� �ٲ�
        max = swap = 0 # max, swap �ʱ�ȭ
        count += 1 # count = count + 1
    num += 1 # num = num + 1
             # ���� �����ǰ�� �����ϱ� ����
print(count) # ���