l, p = map(int, input().split()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
result = [] # ������� ������ result��� list����
for i in range(len(data)) : # �ݺ��� for -> 0���� len(data) - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
    result.append(data[i] - (l * p)) # append�� ����Ͽ� data[i] - (l * p)���� result��� list�� ����
for i in result : # result��� list�� ���Ҹ� ���ʴ�� i�� ����
    print(i, end = ' ') # end�� ����Ͽ� ������ ���� �ʰ� ������ �ְ� i���� ���