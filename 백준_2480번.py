a, b, c = map(int, input().split()) # �� ����
if a == b == c : # ���ǹ� if, elif, else -> ���� ���� 3���� ���
    print(10000 + a * 1000)
elif a == b : # ���� ���� 2���� ���
    print(1000 + a * 100)
elif a == c : # ���� ���� 2���� ���
    print(1000 + a * 100)
elif b == c : # ���� ���� 2���� ���
    print(1000 + b * 100)
else : # ��� �ٸ� ���� ���� ���
    print(100 * max(a, b, c))