a, b = map(int, input().split()) # �� ����
def gcd(a, b) : # �Լ� ���� -> �ִ����� ���ϴ� �Լ�
    while b > 0 : # �ݺ��� while -> b�� 0���� Ŭ ��� �ݺ�
        a, b = b, a % b # ��Ŭ���� ȣ����
    return a # �� ��ȯ
def lcm(a, b) : # �Լ� ���� -> �ּҰ���� ���ϴ� �Լ� 
    return a * b // gcd(a, b) # �� ��ȯ
print(gcd(a, b)) # ���
print(lcm(a, b)) # ���