n = int(input()) # �� ����
def a(n) : # �Լ� ����
    if n <= 1 : # ������ if, else -> n�� 1������ ���� ��ȯ���� n�� ����
        return n # n�� ��ȯ
    else : 
        return a(n - 1) + a(n - 2) # �Ǻ���ġ �� ����
print(a(n)) # ���