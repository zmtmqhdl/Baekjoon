n = int(input()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(input())) # append�� ����Ͽ� ���Ե� ���� data��� list�� ���ҷ� ����
data.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� data�� ���Ҹ� ������������ ����
rank = 1 # ������ ������ rank���� 1�� �ʱ�ȭ
result = 0 # ����� ������ result���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    money = i - (rank - 1) # �� ����
    if money > 0 : # ���ǹ� if -> ���� 1�̻��� ���
        result += money # result = result + money
    rank += 1 # rank = rank + 1
print(result) # ���