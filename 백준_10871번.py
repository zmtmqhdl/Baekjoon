n, x = map(int, input().split()) # �� �Է�
a = list(map(int, input().split())) # list������ �� �Է�
for i in a : # �ݺ��� -> i�� a�� ���� ���ʴ�� ����
    if x > i :
        print(i, sep = ' ') # sep�� ����Ͽ� ��� �� �������� ����