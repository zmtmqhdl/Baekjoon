data = [0, 1] # �Ǻ���ġ ������ ������ data��� list����
n = int(input()) # �� ����
i = 2 # �Ǻ���ġ ������ ���꿡 �ʿ��� i���� ���� �� 2�� ����
while n + 1 != len(data) : # �ݺ��� while -> ���Ե� ���� 1�� ���� ���� len(data)�� ���� ���� ���� ��� �ݺ�
    data.append(data[i - 2] + data[i - 1]) # append�� ����Ͽ� ����� ���� data��� list�� ���ҿ� ����
    i += 1 # i = i + 1
print(data[n]) # ���