t = int(input()) # �� ����
for _ in range(t) : # �ݺ��� for -> t��ŭ �ݺ�
    a, b = map(int, input().split()) # �� ����
    aa, bb = a, b # aa, bb������ a, b������ ���� ���� ����
    while bb != 0 : # �ݺ��� while -> bb�� 0�� �ƴ� ��� �ݺ�
        aa = aa % bb # aa������ aa % bb�� ���� ����
        aa, bb = bb, aa # aa, bb������ bb, aa������ ���� ���� ����
    print(a * b // aa) # ���