import sys # ���̺귯�� ȣ��
a, b = map(int, sys.stdin.readline().split()) # �� ���� -> sys.stdin.readline() = input()
count = 1 # a�� b�� �ٲٴµ� �ʿ��� ������ Ƚ���� ���ϱ� ���� count���� ���� -> a�� b�� �ٲٴµ� �ʿ��� ������ �ּڰ��� 1�� ���ؼ� �����
while a != b : # �ݺ��� while -> a�� b�� ���� �ٸ� ��� �ݺ�
    count += 1 # count = count + 1
    temp = b # b�� a�� ���� �� ���� ��츦 Ȯ���ϱ� ���� temp���� ����
    if b % 10 == 1 : # ���ǹ� if -> b�� ������ �ڸ��� ���ڰ� 1�� ���
        b //= 10 # b = b // 10
    elif b % 2 == 0 : # ���ǹ� if -> b�� ������ �ڸ��� ���ڰ� 0 �Ǵ� 2�� ���
        b //= 2 # b = b // 2
    if b == temp : # ���ǹ� if -> b�� ���õ� ������ �Ұ����� ��� b == temp�� ����
        count = -1
        break # ����
print(count) # ���