n = int(input()) # �׽�Ʈ Ƚ�� ����
plus = 0 # plus �ʱ�ȭ
score = 0 # socre �ʱ�ȭ
for _ in range(n) : # �ݺ��� for
    data = input() # �� ����
    for i in range(len(data)) : # �ݺ��� for -> len(data)�� ����ŭ �ݺ�
        if data[i] == 'O' : # ���ǹ� if, else
            plus += 1 # plus = plus + 1
            score += plus # score = socre + plus
        else :
            plus = 0 # plus �ʱ�ȭ
    print(score) # ���
    score = 0 # score �ʱ�ȭ
    plus = 0 # plus �ʱ�ȭ