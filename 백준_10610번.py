n = list((input())) # ���Ե� ���� ���ҷ� ���� n�̶�� list����
n.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� n�̶�� list�� �������� ����
sum = 0 # sum���� �ʱ�ȭ
for i in n : # �ݸ� for -> n�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    sum += int(i) # sum = sum + int(i)
if sum % 3 != 0 or "0" not in n : # ���ǹ� if, else -> 30�� ����� ���� �ڸ����� 0�̰� �� �ڸ��� ���ڵ��� ������ �� 3���� ������ ����������
    print(-1) # ���
else :
    print("".join(n)) # join�� ����Ͽ� n�̶�� list�� ���Ҹ� ������ �����