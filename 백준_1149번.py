import sys # ���̺귯�� ȣ��
input = sys.stdin.readline # input������ sys.stdin.readline����
data = [] # data��� list����
n = int(input()) # �� ����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(list(map(int, input().split()))) # append�� ����Ͽ� �Էµ� list�� data��� list�� ���ҷ� �߰�
for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
    data[i][0] += min(data[i - 1][1], data[i - 1][2]) # data[i][0] = min(data[i - 1][1], data[i - 1][2]) + data[i][0]
    data[i][1] += min(data[i - 1][0], data[i - 1][2]) # data[i][1] = min(data[i - 1][0], data[i - 1][2]) + data[i][1]
    data[i][2] += min(data[i - 1][0], data[i - 1][1]) # data[i][2] = min(data[i - 1][0], data[i - 1][1]) + data[i][2]
print(min(data[-1])) # min�� ����Ͽ� data��� list�� ������ ���� �� �ּҰ��� ���