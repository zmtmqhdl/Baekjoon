t = int(input()) # �׽�Ʈ Ƚ�� ����
for i in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    a, b = map(int, input().split()) # �� ����
    print("Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(a + b)) # int���� str������ ��ȯ���� +�� ����� ����� �� ����