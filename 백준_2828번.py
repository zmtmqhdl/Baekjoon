n, m = map(int, input().split()) # �� ����
j = int(input()) # �� ����
move = 0 # ������ Ƚ���� ������ move���� �ʱ�ȭ
start = 1 # �ٱ��� ���� ���� ��ġ�� ������ start������ 1����
end = m # �ٱ��� ������ ���� ��ġ�� ������ end������ m����
for _ in range(j) : # �ݺ��� for -> j��ŭ �ݺ�
    apple = int(input()) # �� ����
    if apple < start : # ���ǹ� if, elif -> ����� �ٱ��Ϻ��� ���ʿ� �������� ���
        move += (start - apple) # move = move + (start - apple)
        start = apple # �ٱ��� ���� ���� ��ġ ����
        end = apple + m - 1 # �ٱ��� ������ ���� ��ġ ����
    elif apple > end : # ����� �ٱ��Ϻ��� �����ʿ� �������� ���
        move += (apple - end) # move = move + (apple - end)
        end = apple # �ٱ��� ���� ���� ��ġ ����
        start = end - m + 1 # �ٱ��� ������ ���� ��ġ ����
print(move) # ���