n = int(input()) # �� ����
member = input() # �� ����
count = member.count('LL') # count�� ����Ͽ� member��� ������ LL���ڰ� �� �� �ִ��� Ȯ��
if (count <= 1) : # ���ǹ� if, else -> Ŀ�ü��� 1�� ������ ���
    print(len(member)) # len�� ����Ͽ� member������ ���� ���
else : # Ŀ�ü��� 2�� �̻��� ���
    print(len(member) - count + 1) # ��¤�