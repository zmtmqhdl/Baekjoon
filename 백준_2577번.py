a = int(input()) # �� ����
b = int(input()) # �� ����
c = int(input()) # �� ����
result = list(str(a * b * c)) # a * b * c�� str������ ��ȯ�Ͽ� list�� �� ���ھ� ������ ����
for i in range(10): # �ݺ��� for
    print(result.count(str(i))) # count�� ����� ���� i�� result��� list���� ã�Ƽ� ���� ���