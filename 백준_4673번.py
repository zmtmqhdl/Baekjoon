def d(n) : # �Լ� ����
    n = n + sum(map(int, str(n))) # map(int, str(n)) = [int(n) for i in str(n)]
    return n # �� ��ȯ
NoSelfNumber = set() # NoSelfNumber��� ���� ����
for i in range(1, 10001) : # �ݺ��� for
    NoSelfNumber.add(d(i)) # ������ �ߺ��� ���Ҹ� ���� ���� �Ұ���
for i in range(1, 10001) : # �ݺ��� for
    if i not in NoSelfNumber : # ���ǹ� if
        print(i) # ���