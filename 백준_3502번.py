data = [] # �� list ����
for _ in range(10) : # �ݺ��� for
    n = int(input()) # �� ����
    if n % 42 not in data : # data��� list�� n % 42�� ���� ���ٸ� 
        data.append(n % 42) # n % 42�� ���� data��� list�� ����
print(len(data)) # data��� list �ȿ� ��� �ִ� ������ ���� ���