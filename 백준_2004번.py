n, m = map(int, input().split()) # �� ����
def two_count(i) : # �Լ� ���� -> 2�� ������ ���� �Լ� 
    two = 0 # 2�� ������ ������ two���� �ʱ�ȭ
    while i != 0 : # �ݺ��� while -> i�� 0�� �ƴ� ��� �ݺ� 
        i //= 2 # i = i // 2
        two += i # two = two + i
    return two # two�� ���� ��ȯ
def five_count(i) : # �Լ� ���� -> 5�� ������ ���� �Լ�
    five = 0 # 5�� ������ ������ five���� �ʱ�ȭ
    while i != 0: # �ݺ��� while -> i�� 0�� �ƴ� ��� �ݺ�
        i //= 5 # i = i // 5
        five += i # five = five + i
    return five # five�� ���� ��ȯ
print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m))) # min�� ����Ͽ� 2�� 5�� ���� �� ���� ���� ���