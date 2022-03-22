n = int(input()) # �� ����
data = [] # data��� list����
result = 0 # ������� ������ result���� �ʱ�ȭ
schedule = [False] * 1001 # False���� 1001�� ���� schedule�̶�� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    d, w = map(int, input().split()) # �� ����
    data.append((d, w)) # append�� ����Ͽ� (d, w)�� data��� list�� ���ҷ� ����
data.sort(key = lambda x : x[1], reverse = True) # sort(key = lambda, reverse = True)�� ����ؼ� data��� list�� ���Ҹ� ������ �������� ������������ ����
for day, score in data : # �ݺ��� for -> data��� list�� ���Ҹ� day, score�� �����ϸ� �ݺ�
    i = day # �������� Ȯ���ϱ� ���� ����i�� day����
    while i > 0 and schedule[i] == True : # �ݺ��� while -> i�� ����̰� schedule[i]�� True�� ���
                                          # scheduel[i]�� ���� False�̸� ���� ����
        i -= 1 # i = i - 1
               # �������� ������ ���� ó���� �� �ִ��� Ȯ��
    if i == 0 : # ���ǹ� if, else -> i�� 0�� ���
        continue # �̹� �ݺ����� �ƹ��͵� �������� ����
    else : # i�� 0�� �ƴ� ���
        schedule[i] = True # schedule[i]�� ���� True�� �ٲ� -> i�Ͽ��� �ݺ����� ������ �ִ� ������ �ؾ���
        result += score # result = result + score
print(result) # ���