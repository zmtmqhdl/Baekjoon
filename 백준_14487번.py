n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
data.sort() # sort�� ����Ͽ� data��� list�� ���Ҹ� ������������ ����
del data[-1] # del�� ����Ͽ� data��� list���� ���� ū ���� ���� ���� ����
print(sum(data)) # sum�� ����Ͽ� data��� list�� ������ ���� ���