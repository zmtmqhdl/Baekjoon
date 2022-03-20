n, m = map(int, input().split()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
plus = [] # ������� ������ data��� list����
minus = [] # �������� ������ data��� list����
move = 0 # ������ �Ÿ��� ������ move���� �ʱ�ȭ
max_move = 0 # ���� �ָ� �ִ� å�� ��ġ�� ������ max_move���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i > 0 : # ���ǹ� if, elif -> i�� ����� ���
        plus.append(i) # append�� ����Ͽ� i�� plus��� list�� ���ҷ� �߰� 
    elif i < 0 : # i�� ������ ���
        minus.append(i) # append�� ����Ͽ� i�� minus��� list�� ���ҷ� �߰�
    if abs(i) > abs(max_move) : # ���ǹ� if -> abs�� ����Ͽ� i�� max_move�� ������ ���Ͽ� i�� �� Ŭ ���
        max_move = i # max_move ����
plus.sort(reverse = True) # sort(reverse = True)�� ����Ͽ� plus��� list�� ���Ҹ� ������������ ����
minus.sort() # sort�� ����Ͽ� minus��� list�� ���Ҹ� ������������ ����
for i in range(0, len(plus), m) : # �ݺ��� for -> 0���� len(plus) - 1���� m�� �������� i�� ������� �ݺ�
    if plus[i] != max_move : # ���ǹ� if -> plus[i]�� ���� max_move�� ���� ���� ���
        move += plus[i] # move = move + plus[i]
for i in range(0, len(minus), m) : # �ݺ��� for -> 0���� len(minus) - 1���� m�� �������� i�� �����ϸ� �ݺ�
    if minus[i] != max_move : # ���ǹ� if -> mins[i]�� ���� max_move�� ���� ���� ���
        move += abs(minus[i]) # move = move + abs(minus[i])
move *= 2 # move = move * 2
          # å�� ���� ���ڸ��� ���ƿ��Ƿ� move * 2
move += abs(max_move) # move = move + abs(max_move)
                      # ������ å�� ���� ���ڸ��� ���ƿ��� �ʴ´�.
print(move) # ���