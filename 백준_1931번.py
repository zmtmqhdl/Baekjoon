n = int(input()) # �׽�Ʈ Ƚ�� ����
time = [] # time�̶�� list����
for _ in range(n) : # �ݺ��� for -> n��ŭ �ݺ�
    x, y = map(int, input().split()) # �� ����
    time.append((x, y)) # append�� ����Ͽ� (x, y)�� time�̶�� list�� ���ҷ� �߰�
time.sort() # time�̶�� list�� ������������ ���� -> x�� ��������
time.sort(key = lambda x : x[1]) # time�̶�� list�� ������������ ���� -> y�� ��������
                                 # ȸ�ǰ� ���� �������� ����� �� �ִ� ������ �þ
end = 0 # ȸ�ǰ� ���� �ð��� ������ end���� �ʱ�ȭ
count = 0 # ȸ���� �ִ� ������ ������ count���� �ʱ�ȭ
for a, b in time : # �ݺ��� for -> a, b�� time�̶�� list�� ����� (x, y)������ ���Ҹ� ���ʴ�� �����ϸ� �ݺ�
    if a >= end : # ���ǹ� if -> ȸ�� ���� �ð��� �ֱٿ� ȸ�ǰ� ���� �ð����� ������ ���
        count += 1 # count = count + 1
        end = b # ȸ�ǰ� ���� �ð��� b�� ����
print(count) # ���