import fractions # ���̺귯�� ȣ��
n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
for i in range(1, n) : # �ݺ��� for -> 1���� n -1���� i�� ���ʴ�� �����ϸ� �ݺ�
    a = fractions.Fraction(data[i], data[0]) # fractions.Fraction(����, �и�)�� ����Ͽ� ���м� ����
    print(str(a.denominator) + '/' + str(a.numerator)) # denominator�� ����Ͽ� �и�, numerator�� ����Ͽ� ���ڸ� ã�Ƴ� ���