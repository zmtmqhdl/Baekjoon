a, b= input().split() # �� ����
min = int(a.replace('6', '5')) + int(b.replace('6', '5')) # replace�� ����Ͽ� 6�� 5�� �ٲ㼭 a�� b�� ���� ���� min������ ����
max = int(a.replace('5', '6')) + int(b.replace('5', '6')) # replace�� ����Ͽ� 5�� 6���� �ٲ㼭 a�� b�� ���� ���� max������ ����
print(min, max) # ���