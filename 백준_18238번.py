data = str(input()) # �� ����
time = 0 # ������� ������ time���� �ʱ�ȭ
letter = 'A' # ���� ���� ������ letter������ 'A'����
for i in data : # �ݺ��� for -> data��� ���ڸ� �� ���ھ� ���ʴ�� i�� �����ϸ� �ݺ�
    left = ord(letter) - ord(i) # ord�� ����Ͽ� ���ڸ� �����ڵ�� ����
                                # �������� ������ ���
    right = ord(i) - ord(letter) # ord�� ����Ͽ� ���ڸ� �����ڵ� ����
                                 # ���������� ������ ���
    if left < 0 : # ���ǹ� if -> left�� 0���� ���� ���
        left += 26 # left = left + 26
    if right < 0 : # ���ǹ� if -> right�� 0���� ���� ���
        right += 26 # right = right + 26
    letter = i # letter���� ����
    time += min(right, left) # min�� Ȱ���Ͽ� right, left �߿��� ���� ���� ã��
                             # time = time + min(right, left)
print(time) # ���