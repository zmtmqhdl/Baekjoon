i = 1 # ���̽��� ���� �� i���� ����
while True : # �ݺ��� while -> False�� ���� ������ �ݺ�
    l, p, v = map(int, input().split()) # �� ����
    if l == p == v == 0 : # ���ǹ� if -> l, p, v�� ���� 0�� ���
        break # ����
    count = (v // p) * l # p�� �� l�ϵ��� ����� �� �ִ� ������ ���
    count += min((v % p), l) # count = count + min((v % p), l)
    print(f'Case {i}: {count}') # fstring�� ����Ͽ� ���
    i += 1 # i = i + 1 -> ���̽� �� ������