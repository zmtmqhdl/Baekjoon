n, l = map(int, input().split()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
start = data[0] # �������� ó������ ����ϴ� ����
endata = data[0] + l # �������� ó������ ����ϴ� ���� +  ������ ���� = �������� ������ ����
count = 1 # �������� ������ ������ count���� ����
for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ� 
    if start <= data[i] < endata : # ���ǹ� if, else -> ���� ���� ���� ��ġ�� �������� ������ ������ ��ġ���� ���� ���
        continue # i�� ����ǰ� �ִ� for���� �Ѿ
    else : # ���� ���� ���� ��ġ�� �������� ������ ������ ��ġ���� ū ���
        start = data[i] # �������� ���۵Ǵ� ��ġ�� data[i]�� ����
        endata = data[i] + l  # �������� ������ ������ ��ġ�� data[i] + l�� ����
        count += 1 # count = count + 1
print(count) # ���