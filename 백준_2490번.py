for _ in range(3): # �ݺ��� for -> 3�� �ݺ�
    a = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� a��� list����
    if a.count(0) == 1 : # ���ǹ� if, elif, else -> count�� ����Ͽ� 0�� ���� �ľ�
                         # ��
        print("A") # ���
    elif a.count(0) == 2 : # ��
        print("B") # ���
    elif a.count(0) == 3 : # ��
        print("C") # ���
    elif a.count(0) == 4 : # ��
        print("D") # ���
    else : # ��
        print("E") # ���