import sys # ���̺귯�� ȣ��
import math # ���̺귯�� ȣ��
n, k = map(int, sys.stdin.readline().split()) # �� ����
result = factorial(n) // (factorial(k) * factorial(n - k)) # ����� ����
print(result % 10007) # ���