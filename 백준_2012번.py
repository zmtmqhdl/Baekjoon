import sys # ���̺귯�� ȣ��
n = int(sys.stdin.readline()) # �� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(sys.stdin.readline())) # append�� ����Ͽ� ���Ե� ���� data��� list�� ���ҷ� ����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
result = 0 # ������� ������ result���� �ʱ�ȭ
for i in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    result += abs(data[i] - (i + 1)) # result = result + abs(data[i] - (i + 1))
                                     # abs�� ����Ͽ� ������ ����
print(result) # ���