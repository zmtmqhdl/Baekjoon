n, l = map(int, input().split()) # �� ����
h = list(map(int, input().split())) # ���Ե� ���� ���ҷ� ���� h��� list����
h.sort() # sort�� ����Ͽ� h��� list�� ���Ҹ� ������������ ����
while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
    if len(h) != 0 and l >= h[0] : # ���ǹ� if, elif -> ������ũ�� ���� �� �ִ� ������ �����ϴ� ���
        del h[0] # h��� list�� 0��° index�� ����� ���� ����
    elif len(h) == 0 or l < h[0]: # ������ũ���尡 �� �̻� ���� ������ ���ų� ���̰� ���ڸ� ���
        break # ����
    l += 1 # l = l + 1
print(l) # ���