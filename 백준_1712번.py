a, b, c = map(int, input().split())
if b >= c :
    print(-1)
a, b, c = map(int, input().split()) # �� ����
if b >= c : # ���ǹ� if, else -> b�� c���� Ŀ�� ���ͺб����� �������� ���� ��
    print(-1) # ���
else : 
    print(int(a / (c - b)) + 1) # ������� - ���� = ����)
                                # ������� / ���� + 1 = ���ͺб���