import sys # ���̺귯�� ȣ��
t = int(input()) # �׽�Ʈ Ƚ�� ����
for i in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    a, b = map(int, sys.stdin.readline().rstrip().split()) # sys.stdin.readline().rstrip()�� input()�� ���ؼ� ó���ӵ��� ����
    print(a + b) # ���