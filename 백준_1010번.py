import math # ���̺귯�� ȣ��
t = int(input()) # �� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    n, m = map(int, input().split()) # �� ����
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m - n)) # ������� ������ result������ ����� �����Ͽ� ����
    print(result) # ���