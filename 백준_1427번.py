n = int(input()) # �� ����
data = [i for i in str(n)] # data��� list�� n�� str������ ��ȯ���� ����
data.sort(reverse = True) # sort�� ����� data��� list �������� ����\
                          # reverse = True�� ���� ��������
for i in data : # �ݺ��� for -> i�� data��� list�� ���Ҹ� ���ʴ�� ����
    print(i, end = '') # end = ''�� ����� ������ ���� �ʰ� ���