passenger = 0 # ���� ž�� ���� �°��� ���� ������ passenger���� �ʱ�ȭ
max_passenger = 0 # ������ ž���ߴ� �ִ��ο��� ���� ������ max_passenger���� �ʱ�ȭ
for _ in range(10) :
    out_train, in_train  = map(int, input().split()) # �� ����
    passenger += in_train - out_train # passenger = passenger + in_train - out_train
    max_passenger = max(passenger, max_passenger) # max�� ����Ͽ� passenger, max_passenger �� ū ���� max_passenger�� ����
print(max_passenger) # ���