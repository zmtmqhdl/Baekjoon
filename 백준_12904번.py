s = list(map(str, input())) # ���Ե� ���� ���ҷ� ������ s��� list����
t = list(map(str, input())) # ���Ե� ���� ���ҷ� ������ t��� list����
while len(s) != len(t): # �ݺ��� while -> len�� ����Ͽ� s�� ���̿� t�� ���̰� ���� ���� ���� �ݺ�
    if t[-1] == 'A' : # ���ǹ� if, elif -> t�� ������ ���ڰ� 'A'�� ���
        t.pop() # pop�� ����Ͽ� t�� ������ ���� ����
    elif t[-1] == 'B' : # t�� ������ ���ڰ� 'B'�� ���
        t.pop() # pop�� ����Ͽ� t�� ������ ���� ����
        t = t[::-1] # t
    print(t) # ���
if s == t : # ���ǹ� if, else -> s�� t�� ���� ���
    print(1) # ���
else : # s�� t�� �ٸ� ���
    print(0) # ���