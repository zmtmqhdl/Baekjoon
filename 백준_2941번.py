data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # ũ�ξ�Ƽ�� ���ĺ��� data��� list�� ����
n = str(input()) # �� ����
for i in data : # �ݺ��� for -> i�� data��� list�� ���Ұ��� ���ʴ�� ����
    n = n.replace(i, '*') # replace�� ����Ͽ� i�� ���� *�� ����
print(len(n)) # ����� *�� ������� ���� ���ĺ� �ҹ��ڵ��� ������ len�� ����Ͽ� ���