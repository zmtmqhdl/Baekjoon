s = input() # �� ����
for i in range(97, 123) : # �ݺ��� for -> 97���� 122���� i�� ���ʴ�� �����ϸ� �ݺ�
    result = s.count(chr(i)) # count�� ����Ͽ� chr(i)�� ���� ������ s��� ������ ���� -> chr�� �ƽ�Ű �ڵ�
    print(result, end = ' ') # end�� ����Ͽ� ������ �ΰ� ���