n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
x, y = map(int, input().split()) # �� ����
result = [] # ������ �� A������ ���� �� �ִ� �л����� ���� result��� list������
for i in data : # �ݺ��� data -> data�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if int(i) >= y : # ���ǹ� if -> ����� �� int(i)�� y���� �̻��� ���
        result.append(int(i)) # append�� ����Ͽ� int(i)�� result��� list�� ���ҷ� �߰�
print(round((n * (x / 100))), len(result), sep = ' ') # ���