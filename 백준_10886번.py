v = int(input()) # �� ����
cute = 0 # 1�� ���� Ƚ���� ������ cute���� �ʱ�ȭ
for _ in range(v) : # �ݺ��� for -> v��ŭ �ݺ�
    if int(input()) == 1 : # ���ǹ� if -> ���Ե� ���� 1�� ���
        cute += 1 # cute = cute + 1
if cute > v // 2 : # ���ǹ� if, else -> 1�� ���� Ƚ���� 0���� ���� ���
    print("Junhee is cute!") # ���
else : # 1�� ���� Ƚ������ 0�� ���� Ƚ���� �� ���� ���
    print("Junhee is not cute!") # ���