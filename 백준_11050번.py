import math # ���̺귯�� ȣ��
n, k = map(int, input().split()) # �� ����
result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k)) # ������� ������ result���� ����
print(result) # ���