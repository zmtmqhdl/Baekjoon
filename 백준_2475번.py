data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ������ data��� list����
result = 0 # ������� ������ result���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data�� ���Ҹ� i�� ���ʴ�� �����ϸ� �ݺ�
    result += i ** 2 # result = result + i ** 2
print(result % 10) # ���