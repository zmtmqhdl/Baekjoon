x = int(input()) # �� ����
n = int(input()) # �� ����
result = 0 # ������� ������ result���� �ʱ�ȭ
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    a, b = map(int, input().split()) # ���
    result += a * b # result = result + (a * b)
if result == x : # ���ǹ� if, else -> ������ ����� ��Ȯ�� ���
    print("Yes") # ���
else : # ������ ����� ����Ȯ�� ���
    print("No") # ���