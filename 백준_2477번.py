k = int(input()) # ����� ����
data = [] # data��� list����
for _ in range(6) : # �ݺ��� for -> 6�� �ݺ�
    x, y = map(int, input().split()) # �� ����
    data.append([x, y]) # append�� ����Ͽ� x, y�� 2�� list���·� data��� list�� ���ҷ� ����
w = 0 # ������ �ִ� ���̸� ������ ���� w�ʱ�ȭ
w_idx = 0 # ������ �ִ� ������ index���� ������ ���� w_idx�ʱ�ȭ
h = 0 # ������ �ִ� ���̸� ������ ���� h�ʱ�ȣ��
h_idx = 0 # ������ �ִ� ���̸� index���� ������ ���� h_idx�ʱ�ȭ
for i in range(6) : # �ݺ��� for -> 0���� 5���� ���ʴ�� i�� �����ϸ� �ݺ�
	if data[i][0] == 1 or data[i][0] == 2 : # ���ǹ� if -> ��, �� ������ ���
	    if w < data[i][1] : # ���ǹ� if -> w�� data[i][1]���� ���� ���
	        w = data[i][1] # w�� data[i][1] ����
	        w_idx = i # w�� index���� w_idx�� ����
	elif data[i][0] == 3 or data[i][0] == 4 : # ���ǹ� if -> ��, �� ������ ���
	    if h < data[i][1] : # ���ǹ� if -> h�� data[i][1]���� ���� ���
	        h = data[i][1] # h�� data[i][1] ����
	        h_idx = i # h�� index���� h_idx�� ����
w_sub = abs(data[(w_idx - 1) % 6][1] - data[(w_idx + 1) % 6][1]) # ���� �簢���� ���� ���� ����
h_sub = abs(data[(h_idx - 1) % 6][1] - data[(h_idx + 1) % 6][1]) # ���� �簢���� ���� ���� ����
result = ((w * h) - (w_sub * h_sub)) * k # (ū �簢�� ���� - ���� �簢�� ����) * ����� ���� ����
print(result) # ���