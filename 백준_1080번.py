def reverse(x, y) : # �Լ� ���� -> 3 * 3�� ũ��� ���Ҹ� ������ ���
    for i in range(x, x + 3) : # �ݺ��� for -> x���� x + 2���� ���ʴ�� i�� �����ϸ� �ݺ�
        for j in range(y, y + 3) : # �ݺ��� for -> y���� y + 2���� ���ʴ�� j�� �����ϸ� �ݺ�
            a[i][j] = 1 - a[i][j] # 1 - 1 = 0, 1 - 0 = 1
def check() : # �Լ� ���� -> a�� b�� ���ϴ� ���
    for i in range(n) : # �ݺ��� for -> 0���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
        for j in range(m) : # �ݺ��� for -> 0���� m - 1���� ���ʴ�� j�� �����ϸ� �ݺ�
            if a[i][j] != b[i][j] : # ���ǹ� if -> 3 * 3�� ũ�� ���·� a�� b�� ��
                return False # False ��ȯ
    return True # True ��ȯ
n, m = map(int, input().split()) # �� ����
a = [list(map(int, input())) for _ in range(n)] # 2�� �迭 ���·� ���Ե� ���� ���ҷ� ���� a��� list����
b = [list(map(int, input())) for _ in range(n)] # 2�� �迭 ���·� ���Ե� ���� ���ҷ� ���� b��� list����
count = 0 # ��� a�� ��� b�� �ٲٴµ� �ʿ��� ������ Ƚ���� ������ count���� �ʱ�ȭ
for i in range(n - 2) : # �ݺ��� for -> 0���� n - 1���� ������� i�� �����ϸ� �ݺ�
    for j in range(m - 2) : # �ݺ��� for -> 0���� m - 1���� ���ʴ�� j�� �����ϸ� �ݺ� 
        if a[i][j] != b[i][j]: # ���ǹ� if -> a�� b�� �ٸ� ���
            reverse(i, j) # �Լ� ����
            count += 1 # count = count + 1
if check() == True : # ���ǹ� if -> ��� a�� ��� b�� ��ġ�� ���
    print(count) # ���
else: # ��� a�� ���b�� �ٲ� �� ���� ���
    print(-1) # ���