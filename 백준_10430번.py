A, B, C = map(int, input().split()) # map(�����ų �Լ�, ������ ��)
print((A + B) % C) #������ + ���, �������� �������� % ���, ������ * ���
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)