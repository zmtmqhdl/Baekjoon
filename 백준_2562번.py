data = [] # list ����
for _ in range(9) : # �ݺ��� for -> ��ȣ �ȿ� �ִ� ����ŭ �ݺ�
    data.append(int(input())) # data��� list�� �� ����
print(max(data)) # �ִ� ���
print(data.index(max(data)) + 1) # data��� list���� �ִ��� �ε��� �� + 1 -> �ε����� 0���� ����