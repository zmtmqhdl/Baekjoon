import sys # ���̺귯�� ȣ��
n, m = map(int, sys.stdin.readline().split()) # �� ����
count = 0 # ������� ������ count���� �ʱ�ȭ
s = set() # s��� set����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    s.add(str(sys.stdin.readline())) # add�� ����Ͽ� s��� set�� ���Ե� ���� ���ҷ� �߰�
for _ in range(m) : # �ݺ��� for -> m��ŭ �ݺ�
    data = sys.stdin.readline() # �� ����
    if data in s : # ���ǹ� if -> data�� ���� s��� set�� ���ҷ� �����ϴ� ���
        count += 1 # count = count + 1
print(count) # ���