data = [0, 1] # �ǳ�ġ ���� ������ data��� list����
while len(data) <= 45 : # �ݺ��� while -> len(data)�� ���� 45������ ��� �ݺ�
    data.append(data[-2] + data[-1]) # append�� ����Ͽ� ������ �Ǻ���ġ ���� ����
n = int(input()) # �� ����
print(data[n]) # ���