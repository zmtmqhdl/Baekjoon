data = [] # data��� list����
a = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� a��� list����
data.append(sum(a)) # append�� ����Ͽ� sum(a)�� ���� data��� list�� ���ҷ� ����
b = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� b��� list����
data.append(sum(b)) # append�� ����Ͽ� sum(b)�� ���� data��� list�� ���ҷ� ����
c = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� c��� list����
data.append(sum(c)) # append�� ����Ͽ� sum(c)�� ���� data��� list�� ���ҷ� ����
d = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� d��� list����
data.append(sum(d)) # append�� ����Ͽ� sum(d)�� ���� data��� list�� ���ҷ� ����
e = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� e��� list����
data.append(sum(e)) # append�� ����Ͽ� sum(e)�� ���� data��� list�� ���ҷ� ����
print(data.index(max(data)) + 1, max(data)) # index�� ����Ͽ� ������� ��ȣ�� ����ϰ� max�� ����Ͽ� ������ ������ ���