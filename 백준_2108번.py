import sys # ���̺귯�� ȣ��
from collections import Counter # ���̺귯�� ȣ�� -> from�� ����Ͽ� collections.Counter�� Counter�� ����� �� �ְ� ��
n = int(sys.stdin.readline()) # �� ���� -> sys.stdin.readline() = input()
data = [] # data��� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    data.append(int(sys.stdin.readline())) # append�� ����Ͽ� data��� list�� ���Ե� ���� ���ҷ� �߰�
data.sort() # sort�� ����� data��� list�� ������������ ����
count = Counter(data).most_common(2) # most_common�� ����� data��� list�� ���� ���� �ִ� ���� 2�� ����
                                     # Counter�� �ڷ����� Dictionary
                                     # Counter({'A' : 5, 'B' : 4, 'C' : 3})
print(round(sum(data) / len(data))) # ������ ���
print(data[len(data) // 2]) # �߾Ӱ� ���
if len(data) > 1 : # ������ if, else -> n�� 1���� �Էµ� ���� �ֱ� ����
    if count[0][1] == count[1][1] : # ������ if, else -> �ֺ��� 2�� �̻��� ���
        print(count[1][0]) # �ֺ� �� 2��°�� ���� �� ���
    else :
        print(count[0][0]) # �ֺ� ���
else : # n�� 1�̶�� 
    print(count[0][0]) # ���
print(max(data) - min(data)) # ���� ���