n = int(input()) # �� ����
data = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� data��� list����
result = 0 # ������� ������ result���� �ʱ�ȭ
score = 0 # ���ӵ� ������ ����� score���� �ʱ�ȭ
for i in data : # �ݺ��� for -> data��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
    if i == 1 : # ���ǹ� if , else -> ���� ���� ���
        score += 1 # scroe = score + 1
        result += score # result = result + score
    else : # ���� Ʋ�� ���
        score = 0 # ���ӵ� ���� �ʱ�ȭ
print(result) # ���