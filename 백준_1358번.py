import sys # ���̺귯�� ȣ��
input = sys.stdin.readline # input�� sys.stdin.readline�� �����Ͽ� �� ������ ������ ó��
W, H, X, Y, P = map(int, input().split()) # �� ����
count = 0 # ������� ������ count���� �ʱ�ȭ
for _ in range(P) : # �ݺ��� for -> P��ŭ �ݺ�
    x, y = map(int, input().split()) # �� ����
    if (X <= x <= X + W) and (Y <= y <= Y + H) : # ���ǹ� if -> ������ ���簢�� �ȿ� �ִ� ���
        count +=1 # count = count + 1
        continue # �̹� �ݺ��� �����ϰ� ���� �ݺ� ����
    r = H / 2 # ������ ����
    d1 = ((x - X) ** 2 + (y - (Y + r)) ** 2) ** 0.5 # ���� �ݿ� ����
    d2 = ((x- (X + W)) ** 2 + (y - (Y + r)) ** 2) ** 0.5 # ������ �ݿ� ����
    if d1 <= r or d2 <= r : # ���ǹ� if -> ������ �ݿ� �ȿ� �ִ� ���
        count += 1 # count = count + 1
print(count) # ���