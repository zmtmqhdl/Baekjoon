n = int(input()) # �׽�Ʈ Ƚ�� ����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    money = int(input()) # �� ����
    a = money // 25 # ������ ������ ����
    money -=  25 * (money // 25) # money = money - 25 * (money // 25)
    b = money // 10 # ������ ������ ����
    money -= 10 * (money // 10) # money = money - 10 * (monny // 25)
    c = money // 5 # ������ ������ ����
    money -= 5 * (money // 5) # money = money - 5 * (money // 5)
    print(a, b, c, money) # ���