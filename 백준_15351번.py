n = int(input()) # �� ����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    a = input() # �� ����
    score = 0 # ������ ������ score���� �ʱ�ȭ
    for i in a : # �ݺ��� for -> a���� �� ���ھ� i�� ���ʴ�� �����ϸ� �ݺ�
        if i == ' ' : # ���ǹ� if -> ������ ���
            continue # ����
        else : # ������ ���
            i_score = ord(i) - 64 # ord�� �̿��Ͽ� ���� ���
            score += i_score # score = score + i_score
    if score == 100 : # ���ǹ� if -> score�� 100�� ���
        print('PERFECT LIFE') # ���
    else : # score�� 100�� �ƴ� ���
        print(score) # ���