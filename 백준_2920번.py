data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
ascending = [1, 2, 3, 4, 5, 6, 7, 8] # 1���� 8���� ������������ �� ���Ҹ� ���� ascending��� list����
descending = [8, 7, 6, 5, 4, 3, 2, 1] # 8���� 1���� ������������ �� ���Ҹ� ���� descending��� list����
if data == ascending : # ���ǹ� if, elif -> data��� list�� ���Ұ� ascending��� list�� ���ҿ� ���� ���
    print('ascending') # ���
elif data == descending : # data��� list�� ���Ұ� descending��� list�� ���ҿ� ���� ���
    print('descending') # ���
elif data != ascending and data != descending : # data��� list�� ���Ұ�  ascending��� list�� ����, descending��� list�� ���� �� ��� �Ͱ��� ���� ���� ���
    print('mixed') # ���