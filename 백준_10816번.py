n = int(input()) # �� ����
card = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� card��� list����
m = int(input()) # �� ����
quest = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� quest��� list����
dict = {} # dict��� ���� ����
for i in card : # �ݺ��� for -> card��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i in dict : # ���ǹ� if -> i�� dict��� ������ ���ҷ� �����ϴ� ���
        dict[i] += 1 # dict[i] = dict[i] + 1
    else : # i�� dict��� ������ ���ҷ� �������� �ʴ� ���
        dict[i] = 1 # dict[i]�� ���� 1�� ����
for i in quest : # ���ǹ� if -> quest��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i in dict : # ���ǹ� if -> i�� dict��� ������ ���ҷ� �����ϴ� ���
        print(dict[i], end = ' ') # ���
    else : # i�� dict��� ������ ���ҷ� �������� �ʴ� ���
        print(0, end = ' ') # ���