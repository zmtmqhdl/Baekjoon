n = int(input()) # �� ����
def move(n, a, b, c) : # m�Լ� ����
                       # n�� �Űܾ��ϴ� ��, a�� 1��ž, b�� 2��ž, c�� 3��ž
    if n == 1 : # ���ǹ� if -> ������ 1���� ���� �ٷ� 1��ž���� 3��ž���� �̵�
        print(a, c) # ���
    else :
        move(n - 1, a, c, b) # move�Լ� ����
        print(a, c) # ���
        move(n - 1, b, a, c) # move�Լ� ����
print(2 ** n - 1) # ���
move(n, 1, 2, 3) # �Լ� ����