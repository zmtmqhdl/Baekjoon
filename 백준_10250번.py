t = int(input()) # �׽�Ʈ Ƚ�� ����
for i in range(t): # �ݺ��� for
    h, w, n = map(int, input().split()) # �� ����
    floor = n % h # �� ������ ���ϴ� ����
    room = n // h + 1 # �� ȣ������ ���ϴ� ����
    if floor == 0: # ���ǹ� if -> �ǹ� ������ ����� ���
        room -= 1 # room = room - 1
        floor = h
    print(floor*100 + room) # ���