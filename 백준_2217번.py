n = int(input()) # �׽�Ʈ ȸ�� ����
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(input())) # data��� list�� ���Ե� ���� ���ҷ� �߰�
data.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� data��� list�� ������������ ����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    data[i] = data[i] * (i + 1) # 
print(max(data)) # max�� ����Ͽ� data��� list���� �ִ��� ���