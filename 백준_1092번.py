n = int(input()) # �� ����
crane = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� crane�̶�� list����
m = int(input()) # �� ����
box = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� box��� list����
crane.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� crane�̶�� list�� ���Ҹ� ������������ ����
box.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� box��� list�� ���Ҹ� ������������ ����
time = 0 # ������� ������ time���� �ʱ�ȭ
checked = [0] * m # 0�� m�� ���� checked��� list����
count = 0 # �ű� �ڽ��� ������ ������ count���� �ʱ�ȭ
position = [0] * n # 0�� n�� ���� position��� list���� -> �Űܾ��ϴ� ������ index��
if max(box) > max(crane): # ���ǹ� if, else -> ���� ���ſ� ���ڸ� �ű� �� ���� ���
    print(-1) # ���
else : # ũ������ ���ڸ� ��� �ű� �� �ִ� ���
    while count < len(box) : # �ݺ��� while -> ���ڸ� �� �ű��� �ʾ��� ��� �ݺ�
        for i in range(n) : # �ݺ��� for -> 0���� n - 1���� i�� ���ʴ�� �����ϸ� �ݺ�
            while position[i] < len(box) : # �ݺ��� while -> �Űܾ��ϴ� ���ڰ� ���� ��� �ݺ�
                if not checked[position[i]] and crane[i] >= box[position[i]] : # ���ǹ� if -> ���ڸ� �ű��� �ʾҰ� ũ������ ���ڸ� �ű� �� �ִ� ���
                    checked[position[i]] = True # ���ڸ� �Ű����Ƿ� checked���� True�� ����
                    position[i] += 1 # position[i] = position[i] + 1
                    count += 1 # count = count + 1
                    break # ����
                position[i] += 1 # position[i] = position[i] + 1
        time += 1 # time = time + 1
    print(time) # ���