a, b = map(int, input().split()) # �� ����
n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(input())) # append�� ����Ͽ� �Էµ� ���� data��� list�� ���ҷ� �߰�
b_plus = b_minus = b # b�� ���� 1�� �������� �����ذ� b_plus, b_minus���� ����
while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    if b_plus == a or b_minus == a : # ���ǹ� if, elif -> b_plus, b_minus�� ���� a�� ���� ���
        print(abs(b - a)) # abs�� ����Ͽ� b - a�� ���� ������ ���� �� ���
        break # ����
    elif b_plus in data : # b_plus�� ���� data��� list�� �����ϴ� ���
        print(b_plus - b + 1) # ���
        break # ����
    elif b_minus in data : # b_minus�� ���� data��� list�� �����ϴ� ���
        print(b - b_minus + 1) # ���
        break # ����
    b_plus += 1 # b_plus = b_plus + 1
    b_minus -= 1 # b_minus = b_minus - 1