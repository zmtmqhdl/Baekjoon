data = [] # data��� list����
for _ in range(5) : # �ݺ��� for -> 5ȸ �ݺ�
    data.append(int(input())) # append�� ����Ͽ� ���Ե� ���� data�� ���ҷ� ����
print(min(data[0], data[1], data[2]) + min(data[3], data[4]) - 50) # min�� ����Ͽ� �ּڰ� ���